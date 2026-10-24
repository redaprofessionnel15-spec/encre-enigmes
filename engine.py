"""Encre & Énigmes — Shorts engine v2.

python3 engine.py spec.json out.mp4          full render
PREVIEW=1.0,5.5 python3 engine.py spec.json x.mp4   still frames only
"""
import json, math, os, re, subprocess, sys, random
import numpy as np
import soundfile as sf
import skia
from scipy import signal

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from character import draw_owl

W, H, FPS = 1080, 1920, 30
SR = 44100
ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = {"title": f"{ROOT}/fonts/Cinzel-ExtraBold-static.ttf",
         "sub": f"{ROOT}/fonts/Cormorant-SemiBoldItalic-static.ttf",
         "cap": f"{ROOT}/fonts/Inter-ExtraBold.otf"}
KOKORO_DIR = os.environ.get("KOKORO_DIR", os.path.expanduser("~/kokoro"))

spec_path, out_path = sys.argv[1], sys.argv[2]
spec = json.load(open(spec_path))
SPEC_DIR = os.path.dirname(os.path.abspath(spec_path))
if spec.get("narration"):
    # paths in the spec are relative to the spec file
    spec["narration"] = os.path.join(SPEC_DIR, spec["narration"])
    raw = spec.get("voice_raw") and os.path.join(SPEC_DIR, spec["voice_raw"])
    if not os.path.exists(spec["narration"]) and raw and os.path.exists(raw):
        subprocess.run([sys.executable, f"{ROOT}/tighten_voice.py", raw, spec["narration"],
                        str(spec.get("voice_tempo", 1.06))], check=True)
SEGS = spec["segments"]
work = os.path.abspath(os.path.splitext(out_path)[0] + "_work")
os.makedirs(work, exist_ok=True)
TF = {k: skia.Typeface.MakeFromFile(p) for k, p in FONTS.items()}

def font(kind, size):
    f = skia.Font(TF[kind], size); f.setEdging(skia.Font.Edging.kAntiAlias); return f

# =================================================================== VOICE
try:
    from kokoro_onnx import Kokoro
    kok = Kokoro(f"{KOKORO_DIR}/kokoro-v1.0.onnx", f"{KOKORO_DIR}/voices-v1.0.bin")
except Exception as _e:  # Kokoro is only required when there is no narration file
    if not spec.get("narration"):
        raise
    kok = None
    from kokoro_onnx.tokenizer import Tokenizer
    _tok = Tokenizer()  # espeak phonemizer only: same weights, no model download
VOICE = spec.get("voice", "ff_siwis")
LANG_TAG = re.compile(r"\([a-z]{2,3}(-[a-z]+)?\)")

def phon(text):
    tok = kok.tokenizer if kok is not None else _tok
    return LANG_TAG.sub("", tok.phonemize(text, lang="fr-fr")).strip()

def sentences(t):
    return [p for p in re.split(r'(?<=[.!?…:])\s+', t.strip()) if p]

def clean(w):
    return re.sub(r"[^\wàâäéèêëîïôöùûüçœ'’-]", "", w.lower())

voice_parts, words, chunks, seg_bounds = [], [], [], []
ph_log = []

def tokens(ct):
    return [w for w in re.split(r"[ \t\n]+", re.sub(r"\s+([!?:;»])", "\u00a0\\1", ct.strip())) if w]

def word_weights(ct, st):
    wl = tokens(ct); tw = st.split()
    out = []
    for i, w in enumerate(wl):
        src = tw[i] if len(tw) == len(wl) else w
        out.append(len(phon(src)) + 2)
    return wl, out

if spec.get("narration"):
    # ---------- external narration (e.g. ElevenLabs): align the script on the audio's pauses
    import soundfile as _sf
    voice, vsr = _sf.read(spec["narration"])
    if voice.ndim > 1: voice = voice.mean(axis=1)
    voice = np.concatenate([voice.astype(np.float32), np.zeros(int(.6 * vsr), np.float32)])
    hop = int(.01 * vsr)
    rms = np.array([np.sqrt(np.mean(voice[i:i + hop] ** 2)) for i in range(0, len(voice) - hop, hop)])
    thr = np.percentile(rms[rms > 1e-4], 90) * 0.06
    sil = rms < thr
    pauses = []; i = 0
    while i < len(sil):
        if sil[i]:
            j = i
            while j < len(sil) and sil[j]: j += 1
            if (j - i) * .01 >= .1: pauses.append((i * .01, j * .01))
            i = j
        else: i += 1
    on = pauses[0][1] if pauses and pauses[0][0] < .05 else 0.0
    off = pauses[-1][0] if pauses and pauses[-1][1] >= len(sil) * .01 - .05 else len(voice) / vsr
    inner = [p for p in pauses if p[0] > on + .05 and p[1] < off - .05]
    # phrases split on punctuation, across all segments
    phrases = []   # dict(seg, words, weights, strong)
    for si, seg in enumerate(SEGS):
        ct, st = seg.get("caption", seg["tts"]), seg["tts"]
        wl, wts = word_weights(ct, st)
        cur_w, cur_t = [], []
        for w, wt in zip(wl, wts):
            cur_w.append(w); cur_t.append(wt)
            if re.search(r"[,;:.!?…]$", w):
                phrases.append(dict(seg=si, words=cur_w, wts=cur_t, strong=bool(re.search(r"[.!?…:]$", w))))
                cur_w, cur_t = [], []
        if cur_w: phrases.append(dict(seg=si, words=cur_w, wts=cur_t, strong=True))
        ph_log.append(f"[{si}] {st}\n     {phon(st)}")
    Wtot = sum(sum(p["wts"]) for p in phrases)
    cum = np.cumsum([sum(p["wts"]) for p in phrases])
    exp_b = [on + (off - on) * c / Wtot for c in cum[:-1]]          # expected boundary times
    m, n = len(exp_b), len(inner)
    INF = 1e9
    dp = np.full((m + 1, n + 1), INF); bk = np.zeros((m + 1, n + 1), int)
    dp[0, 0] = 0
    for j in range(1, n + 1): dp[0, j] = dp[0, j - 1] + 1.2 * (inner[j - 1][1] - inner[j - 1][0]); bk[0, j] = 1
    for i_ in range(1, m + 1):
        miss = 2.0 if phrases[i_ - 1]["strong"] else .35
        dp[i_, 0] = dp[i_ - 1, 0] + miss; bk[i_, 0] = 2
        for j in range(1, n + 1):
            pj = inner[j - 1]; mid = (pj[0] + pj[1]) / 2; dur = pj[1] - pj[0]
            c_match = dp[i_ - 1, j - 1] + abs(exp_b[i_ - 1] - mid) - (.3 * dur if phrases[i_ - 1]["strong"] else 0)
            c_skip = dp[i_, j - 1] + 1.2 * dur
            c_miss = dp[i_ - 1, j] + miss
            best = min(c_match, c_skip, c_miss)
            dp[i_, j] = best; bk[i_, j] = 0 if best == c_match else (1 if best == c_skip else 2)
    match = [None] * m; i_, j = m, n
    while i_ > 0 or j > 0:
        b_ = bk[i_, j] if (i_ > 0 and j > 0) else (1 if i_ == 0 else 2)
        if b_ == 0: match[i_ - 1] = inner[j - 1]; i_ -= 1; j -= 1
        elif b_ == 1: j -= 1
        else: i_ -= 1
    # boundary (end_of_phrase, start_of_next) times; interpolate unmatched ones
    bnd = []
    for k in range(m):
        bnd.append(match[k] if match[k] else None)
    known = [(-1, (on, on))] + [(k, b) for k, b in enumerate(bnd) if b] + [(m, (off, off))]
    for k in range(m):
        if bnd[k] is None:
            lo = max(x for x in known if x[0] < k); hi = min(x for x in known if x[0] > k)
            c_lo = cum[lo[0]] if lo[0] >= 0 else 0; c_hi = cum[hi[0]] if hi[0] < m else Wtot
            tt_ = lo[1][1] + (hi[1][0] - lo[1][1]) * (cum[k] - c_lo) / max(1e-6, c_hi - c_lo)
            bnd[k] = (tt_, tt_)
    starts = [on] + [b[1] for b in bnd]; ends = [b[0] for b in bnd] + [off]
    seg_first = {}
    for k, ph in enumerate(phrases):
        ps, pe = starts[k], ends[k]
        tot = sum(ph["wts"]); cur = ps; chunk = []
        seg_first.setdefault(ph["seg"], k)
        for i2, (w, wt) in enumerate(zip(ph["words"], ph["wts"])):
            wd = (pe - ps) * wt / tot
            words.append(dict(t0=cur, t1=cur + wd, text=w, clean=clean(w), seg=ph["seg"]))
            chunk.append(len(words) - 1); cur += wd
            if len(chunk) >= 4 or i2 == len(ph["words"]) - 1:
                chunks.append(dict(t0=words[chunk[0]]["t0"], t1=words[chunk[-1]]["t1"], w=chunk)); chunk = []
    TOTAL = len(voice) / vsr
    for si in range(len(SEGS)):
        k0 = seg_first[si]
        a_ = 0.0 if si == 0 else (ends[k0 - 1] + starts[k0]) / 2
        b_ = TOTAL if si == len(SEGS) - 1 else (ends[seg_first[si + 1] - 1] + starts[seg_first[si + 1]]) / 2
        seg_bounds.append((a_, b_))
    open(f"{work}/alignment.txt", "w").write("\n".join(
        f"{starts[k]:6.2f}-{ends[k]:6.2f} [{p['seg']}] {' '.join(p['words'])}" for k, p in enumerate(phrases)))
else:
  t = 0.0
  for si, seg in enumerate(SEGS):
    s0 = t
    spd = seg.get("speed", spec.get("speed", 1.06))
    tts_s, cap_s = sentences(seg["tts"]), sentences(seg.get("caption", seg["tts"]))
    if len(tts_s) != len(cap_s):
        cap_s = tts_s
    for st, ct in zip(tts_s, cap_s):
        ph = phon(st)
        for a_fix, b_fix in spec.get("phoneme_fix", []):
            ph = ph.replace(a_fix, b_fix)
        ph_log.append(f"[{si}] {st}\n     {ph}")
        smp, vsr = kok.create(ph, voice=VOICE, speed=spd, is_phonemes=True)
        a = np.abs(smp); idx = np.where(a > 0.008)[0]
        if len(idx):
            smp = smp[max(0, idx[0] - 400): idx[-1] + 1600]
        d = len(smp) / vsr
        wl, weights = word_weights(ct, st)
        weights = [w + (6 if re.search(r"[,;:]$", wl[i]) else 0) for i, w in enumerate(weights)]
        tot = sum(weights)
        cur, chunk = t, []
        for i, w in enumerate(wl):
            wd = d * weights[i] / tot
            words.append(dict(t0=cur, t1=cur + wd, text=w, clean=clean(w), seg=si))
            chunk.append(len(words) - 1); cur += wd
            if len(chunk) >= 4 or re.search(r"[,;:.!?…]$", w) or i == len(wl) - 1:
                chunks.append(dict(t0=words[chunk[0]]["t0"], t1=words[chunk[-1]]["t1"], w=chunk)); chunk = []
        gap = 0.5 if st.endswith("…") else (0.26 if seg.get("dramatic") else 0.14)
        voice_parts += [smp.astype(np.float32), np.zeros(int(gap * vsr), np.float32)]
        t += d + gap
    tail = seg.get("tail", 0.18)
    voice_parts.append(np.zeros(int(tail * vsr), np.float32)); t += tail
    seg_bounds.append((s0, t))
  voice = np.concatenate(voice_parts)
  TOTAL = len(voice) / vsr
open(f"{work}/phonemes.txt", "w").write("\n".join(ph_log))
NF = int(math.ceil(TOTAL * FPS))

def word_time(si, key):
    if not key: return None
    key, n = (key.split("#") + ["1"])[:2]
    n = int(n); c = 0
    for w in words:
        if w["seg"] == si and w["clean"].startswith(key.lower()):
            c += 1
            if c == n: return w["t0"]
    return None

# lip-sync envelope + slow gesture curve
env = np.zeros(NF); win = int(vsr / FPS)
for f in range(NF):
    c = int(f / FPS * vsr); s_ = voice[max(0, c - win): c + win]
    env[f] = math.sqrt(float(np.mean(s_ ** 2))) if len(s_) else 0
ref = np.percentile(env[env > .002], 95) if np.any(env > .002) else 1
env = np.clip(env / ref, 0, 1) ** .7
ENV = np.zeros(NF); GEST = np.zeros(NF)
for f in range(NF):
    p_ = ENV[f - 1] if f else 0
    ENV[f] = p_ + (env[f] - p_) * (.65 if env[f] > p_ else .3)
    g_ = GEST[f - 1] if f else 0
    GEST[f] = g_ + (min(1, ENV[f] * 1.3) - g_) * .06

# =================================================================== AUDIO
N = int((TOTAL + 1) * SR); tt = np.arange(N) / SR
rng = np.random.default_rng(7)
music = np.zeros((N, 2)); sfx = np.zeros((N, 2))

def put(bus, sig, at, gain=1.0, pan=0.0):
    s0 = int(at * SR)
    if s0 >= N or s0 < 0: return
    e = min(N, s0 + len(sig)); seg_ = sig[:e - s0] * gain
    bus[s0:e, 0] += seg_ * (1 - max(0, pan)); bus[s0:e, 1] += seg_ * (1 + min(0, pan))

def saw(freq, n, harm=8):
    k = np.arange(n) / SR; out = np.zeros(n)
    for h in range(1, harm + 1):
        out += np.sin(2 * np.pi * freq * h * k) / h
    return out

# chord pad (A minor), detuned saws, low-passed; swells with "tension"
NOTE = lambda m: 440 * 2 ** ((m - 69) / 12)
PROG = [[45, 48, 52, 57], [41, 45, 48, 53], [38, 41, 45, 50], [40, 44, 47, 52]]
tension = np.zeros(N)
for si, seg in enumerate(SEGS):
    a_, b_ = seg_bounds[si]
    tension[int(a_ * SR):int(b_ * SR)] = seg.get("tension", .4)
tension = np.convolve(tension, np.ones(SR) / SR, "same")
CL = 4.8
for i in range(int(TOTAL / CL) + 2):
    s0 = int(i * CL * SR); ln = int((CL + 2.0) * SR)
    if s0 >= N: break
    ln = min(ln, N - s0); k = np.arange(ln) / SR
    envp = np.minimum(1, k / 1.8) * np.clip((CL + 2.0 - k) / 2.0, 0, 1)
    blk = np.zeros((ln, 2))
    for m in PROG[i % 4]:
        for j, det in enumerate((-0.006, 0, 0.007)):
            o = saw(NOTE(m) * (1 + det), ln, 7)
            blk[:, j % 2] += o * .5; blk[:, (j + 1) % 2] += o * .25
    blk[:, 0] += 0.8 * np.sin(2 * np.pi * NOTE(PROG[i % 4][0] - 12) * k)
    blk[:, 1] += 0.8 * np.sin(2 * np.pi * NOTE(PROG[i % 4][0] - 12) * k)
    music[s0:s0 + ln] += blk * envp[:, None] * .05
sos = signal.butter(2, 1100, "low", fs=SR, output="sos")
music = signal.sosfilt(sos, music, axis=0)
music *= (0.55 + 0.9 * tension)[:, None]

def bell(freq, d=1.6):
    k = np.arange(int(d * SR)) / SR
    return (np.sin(2 * np.pi * freq * k) + .35 * np.sin(2 * np.pi * freq * 2.76 * k) * np.exp(-k * 4)) * np.exp(-k * 2.6)

def motif(at, gain=.22):
    for i, m in enumerate([81, 84, 88, 86, 84, 83, 81]):
        put(music, bell(NOTE(m)), at + i * .28, gain, pan=(-.3 if i % 2 else .3))

def taiko(d=1.1, f0=70):
    k = np.arange(int(d * SR)) / SR
    s = np.sin(2 * np.pi * (f0 - 30 * k) * k) * np.exp(-k * 5)
    s += .35 * signal.sosfilt(signal.butter(2, 400, "low", fs=SR, output="sos"), rng.standard_normal(len(k))) * np.exp(-k * 18)
    return s

def boom(d=1.6):
    k = np.arange(int(d * SR)) / SR
    s = np.sin(2 * np.pi * (52 - 22 * k) * k) * np.exp(-k * 2.8)
    nz = signal.sosfilt(signal.butter(2, 900, "low", fs=SR, output="sos"), rng.standard_normal(len(k)))
    return s + .9 * nz * np.exp(-k * 4.5)

def riser(d=1.6):
    k = np.arange(int(d * SR)) / SR
    nz = rng.standard_normal(len(k))
    out = np.zeros(len(k)); seg_n = 8
    for i in range(seg_n):
        a_, b_ = i * len(k) // seg_n, (i + 1) * len(k) // seg_n
        fc = 300 + 3500 * (i / seg_n) ** 2
        out[a_:b_] = signal.sosfilt(signal.butter(2, fc, "low", fs=SR, output="sos"), nz[a_:b_])
    out += .3 * np.sin(2 * np.pi * (180 + 500 * (k / d) ** 2) * k)
    return out * (k / d) ** 2

def whoosh(d=.5):
    k = np.arange(int(d * SR)) / SR; nz = rng.standard_normal(len(k))
    s = signal.sosfilt(signal.butter(2, [400, 2600], "band", fs=SR, output="sos"), nz)
    return s * np.sin(np.pi * k / d) ** 2

def thud():
    k = np.arange(int(.4 * SR)) / SR
    return np.sin(2 * np.pi * 90 * k) * np.exp(-k * 14) + .25 * rng.standard_normal(len(k)) * np.exp(-k * 70)

def tick():
    k = np.arange(int(.035 * SR)) / SR
    return np.sin(2 * np.pi * 2300 * k) * np.exp(-k * 150)

def pop():
    k = np.arange(int(.25 * SR)) / SR
    return np.sin(2 * np.pi * (500 + 900 * k) * k) * np.exp(-k * 18)

def splash(d=1.0):
    k = np.arange(int(d * SR)) / SR
    return signal.sosfilt(signal.butter(2, [300, 3000], "band", fs=SR, output="sos"), rng.standard_normal(len(k))) * np.exp(-k * 3.5)

for (a_, _) in seg_bounds[1:]:
    put(sfx, whoosh(), a_ - .3, .35)
motif(0.05, .16)

# reverb (synthetic IR) on the music + sfx buses
irk = np.arange(int(1.7 * SR)) / SR
ir = rng.standard_normal(len(irk)) * np.exp(-irk * 3.2)
ir = signal.sosfilt(signal.butter(2, 3500, "low", fs=SR, output="sos"), ir); ir /= np.sqrt(np.sum(ir ** 2))

# =================================================================== DRAW HELPERS
def col(h, a=255):
    h = h.lstrip("#"); return skia.ColorSetARGB(int(max(0, min(255, a))), int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def P(c, a=255, stroke=0):
    p = skia.Paint(AntiAlias=True, Color=col(c, a))
    if stroke:
        p.setStyle(skia.Paint.kStroke_Style); p.setStrokeWidth(stroke)
        p.setStrokeCap(skia.Paint.kRound_Cap); p.setStrokeJoin(skia.Paint.kRound_Join)
    return p

def lin(p0, p1, cols, pos=None):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear(points=[p0, p1], colors=[col(*c) if isinstance(c, tuple) else col(c) for c in cols], positions=pos))
    return p

def rad(c, r, cols, pos=None):
    p = skia.Paint(AntiAlias=True)
    r = max(r, 0.5)
    p.setShader(skia.GradientShader.MakeRadial(center=c, radius=r, colors=[col(*x) if isinstance(x, tuple) else col(x) for x in cols], positions=pos))
    return p

def clamp(x, a=0., b=1.): return max(a, min(b, x))
def eo(x): x = clamp(x); return 1 - (1 - x) ** 3
def eio(x): x = clamp(x); return 3 * x * x - 2 * x * x * x
def eback(x, s=1.7): x = clamp(x) - 1; return x * x * ((s + 1) * x + s) + 1
def ebounce(x):
    x = clamp(x); n1, d1 = 7.5625, 2.75
    if x < 1 / d1: return n1 * x * x
    if x < 2 / d1: x -= 1.5 / d1; return n1 * x * x + .75
    if x < 2.5 / d1: x -= 2.25 / d1; return n1 * x * x + .9375
    x -= 2.625 / d1; return n1 * x * x + .984375

def text_c(cv, s, x, y, f, c, a=255, shadow=True):
    w = f.measureText(s)
    if shadow: cv.drawString(s, x - w / 2 + 4, y + 6, f, P("#000000", a * .55))
    cv.drawString(s, x - w / 2, y, f, P(c, a)); return w

def gold(cv, s, x, y, size, a=255):
    f = font("title", size); w = f.measureText(s)
    cv.drawString(s, x - w / 2 + 6, y + 8, f, P("#000000", a * .6))
    cv.drawString(s, x - w / 2, y, f, lin((0, y - size), (0, y), [("#FCE9B6", a), ("#E2B661", a), ("#A8702E", a)], [0, .55, 1]))
    return w

def fit(s, kind, start, maxw):
    z = start
    while z > 28 and font(kind, z).measureText(s) > maxw: z -= 4
    return z

# =================================================================== BACKGROUND
random.seed(5)
STARS = [(random.uniform(0, W), random.uniform(0, H), random.choice([1, 1.3, 1.8, 2.4]), random.uniform(0, 6.28), random.uniform(4, 14)) for _ in range(230)]
DUST = [(random.uniform(0, W), random.uniform(0, H), random.uniform(1.5, 4.5), random.uniform(0, 6.28), random.uniform(10, 30)) for _ in range(50)]
GRAIN = []
for g in range(6):
    n_ = (np.random.default_rng(g).integers(0, 255, (H // 2, W // 2), dtype=np.uint8))
    rgba = np.zeros((H // 2, W // 2, 4), np.uint8); rgba[..., :3] = n_[..., None]; rgba[..., 3] = 255
    GRAIN.append(skia.Image.fromarray(rgba, colorType=skia.kRGBA_8888_ColorType))

def background(cv, t, warm=0.0):
    cv.drawRect(skia.Rect.MakeWH(W, H), lin((0, 0), (0, H), ["#22305A", "#121B36", "#060A15"], [0, .5, 1]))
    br = .75 + .25 * math.sin(t * 1.3)
    cv.drawRect(skia.Rect.MakeWH(W, H), rad((W / 2, 620), 600, [("#D6A650", 60 * br + 50 * warm), ("#D6A650", 0)]))
    gp = P("#D6A650", 14, 2); off = (t * 8) % 120
    for i in range(-1, 11): cv.drawLine(i * 120 + off, 0, i * 120 + off + 40, H, gp)
    for j in range(18): cv.drawLine(0, j * 120 + off * .6, W, j * 120 + off * .6 + 30, gp)
    for (x, y, r, ph, sp) in STARS:
        cv.drawCircle(x, (y - t * sp) % H, r, P("#F3E2B8", 70 + 120 * (.5 + .5 * math.sin(ph + t * 2.2))))

def foreground(cv, t, f):
    for (x, y, r, ph, sp) in DUST:
        cv.drawCircle(x + 25 * math.sin(ph + t * .7), (y - t * sp) % H, r, P("#E7BD6A", 80 + 60 * math.sin(ph + t)))
    cv.drawRect(skia.Rect.MakeWH(W, H), rad((W / 2, H * .45), H * .78, [("#000000", 0), ("#000000", 0), ("#000000", 175)], [0, .55, 1]))
    gp = skia.Paint(); gp.setAlphaf(.06); gp.setBlendMode(skia.BlendMode.kOverlay)
    cv.drawImageRect(GRAIN[f % 6], skia.Rect.MakeWH(W, H), skia.SamplingOptions(), gp)

def rays(cv, cx, cy, t, a=40):
    for k in range(9):
        ang = math.radians(k * 40 + t * 6)
        pth = skia.Path(); pth.moveTo(cx, cy)
        for da in (-.09, .09):
            pth.lineTo(cx + 1400 * math.cos(ang + da), cy + 1400 * math.sin(ang + da))
        pth.close()
        cv.drawPath(pth, rad((cx, cy), 900, [("#F3D48F", a), ("#F3D48F", 0)]))

def header(cv, t):
    text_c(cv, "ENCRE & ÉNIGMES", W / 2, 150, font("title", 40), "#D6A650", shadow=False)
    bx, bw = (W - 560) / 2, 560
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, 180, bw, 8), 4, 4), P("#D6A650", 55))
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(bx, 180, bw * clamp(t / TOTAL), 8), 4, 4), P("#F0CF85"))

# =================================================================== PROPS
def watch(cv, cx, cy, R, hdeg, mdeg, sdeg, a=255, glow=0.0):
    if R < 2: return
    if glow > 0: cv.drawCircle(cx, cy, R * 1.7, rad((cx, cy), R * 1.7, [("#E8533A", 110 * glow), ("#E8533A", 0)]))
    cv.drawCircle(cx, cy - R - 26, 22, P("#C9963F", a, 9))
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 20, cy - R - 16, 40, 26), 6, 6), P("#D6A650", a))
    cv.drawCircle(cx, cy, R, lin((cx - R, cy - R), (cx + R, cy + R), [("#F7DD9C", a), ("#C48D3C", a), ("#8A5A22", a)], [0, .5, 1]))
    cv.drawCircle(cx, cy, R * .88, P("#F4E8CC", a)); cv.drawCircle(cx, cy, R * .88, P("#B0823A", a, 3))
    for k in range(60):
        an = math.radians(k * 6); big = k % 5 == 0; r1, r2 = R * (.74 if big else .80), R * .84
        cv.drawLine(cx + r1 * math.sin(an), cy - r1 * math.cos(an), cx + r2 * math.sin(an), cy - r2 * math.cos(an), P("#3A2A18", a, 5 if big else 2))
    nf = font("title", R * .17)
    for lab, k in (("XII", 0), ("III", 3), ("VI", 6), ("IX", 9)):
        an = math.radians(k * 30); r = R * .6; w = nf.measureText(lab)
        cv.drawString(lab, cx + r * math.sin(an) - w / 2, cy - r * math.cos(an) + R * .06, nf, P("#3A2A18", a))
    for deg, L, wd, c_ in ((hdeg, .42, 12, "#2A1E12"), (mdeg, .66, 8, "#2A1E12"), (sdeg, .72, 3, "#B23A2E")):
        an = math.radians(deg); cv.drawLine(cx, cy, cx + R * L * math.sin(an), cy - R * L * math.cos(an), P(c_, a, wd))
    cv.drawCircle(cx, cy, 12, P("#B23A2E", a))
    cv.drawOval(skia.Rect.MakeXYWH(cx - R * .55, cy - R * .75, R * .5, R * .3), P("#FFFFFF", a * .18))

def compass(cv, cx, cy, R, rot, a=255):
    cv.save(); cv.translate(cx, cy); cv.rotate(rot)
    cv.drawCircle(0, 0, R, P("#D6A650", a * .8, 4)); cv.drawCircle(0, 0, R * .84, P("#D6A650", a * .45, 2))
    for k in range(72):
        an = math.radians(k * 5); r1 = R * (.90 if k % 2 else .86)
        cv.drawLine(r1 * math.cos(an), r1 * math.sin(an), R * math.cos(an), R * math.sin(an), P("#D6A650", a * .6, 2))
    for k in range(8):
        an = math.radians(k * 45 - 90); L = R * (.8 if k % 2 == 0 else .5); w = R * .1
        pth = skia.Path(); pth.moveTo(w * math.cos(an - math.pi / 2), w * math.sin(an - math.pi / 2))
        pth.lineTo(L * math.cos(an), L * math.sin(an)); pth.lineTo(w * math.cos(an + math.pi / 2), w * math.sin(an + math.pi / 2)); pth.close()
        cv.drawPath(pth, P("#E2B661" if k % 2 == 0 else "#9C6B28", a * (.9 if k % 2 == 0 else .6)))
    cv.restore()

def pin(cv, x, y, s):
    pth = skia.Path(); pth.moveTo(x, y)
    pth.cubicTo(x - 40 * s, y - 60 * s, x - 62 * s, y - 90 * s, x - 62 * s, y - 120 * s)
    pth.arcTo(skia.Rect.MakeXYWH(x - 62 * s, y - 182 * s, 124 * s, 124 * s), 180, 180, False)
    pth.cubicTo(x + 62 * s, y - 90 * s, x + 40 * s, y - 60 * s, x, y); pth.close()
    cv.drawPath(pth, lin((x, y - 180 * s), (x, y), ["#E2564A", "#9C2418"])); cv.drawPath(pth, P("#5E140C", 255, 4))
    cv.drawCircle(x, y - 120 * s, 24 * s, P("#F4E8CC"))

def waves(cv, y0, y1, t, layers=3, amp=12):
    for L in range(layers):
        yy = y0 + (y1 - y0) * L / layers
        pts = [(x, yy + amp * math.sin(x / (90 + 20 * L) + t * (1.4 + .3 * L) + L)) for x in range(0, W + 41, 40)]
        pth = skia.Path(); pth.moveTo(0, H)
        for x, y in pts: pth.lineTo(x, y)
        pth.lineTo(W, H); pth.close()
        cv.drawPath(pth, P(["#17284D", "#101C38", "#0A1428"][L % 3], 240))
        cr = skia.Path(); cr.moveTo(*pts[0])
        for x, y in pts[1:]: cr.lineTo(x, y)
        cv.drawPath(cr, P("#D6A650", 70 - 15 * L, 3))

def palm(cv, x, y, s, t):
    cv.save(); cv.translate(x, y); cv.scale(s, s)
    tr = skia.Path(); tr.moveTo(0, 0); tr.quadTo(18, -80, 6, -160); cv.drawPath(tr, P("#070B16", 255, 14))
    for k in range(6):
        an = -150 + k * 50 + 5 * math.sin(t * 1.5 + k)
        ex, ey = 6 + 95 * math.cos(math.radians(an)), -160 + 95 * math.sin(math.radians(an)) + 30
        lf = skia.Path(); lf.moveTo(6, -160); lf.quadTo((6 + ex) / 2, -200, ex, ey); cv.drawPath(lf, P("#070B16", 255, 12))
    cv.restore()

def palace(cv, x, y, s, fire=0., t=0.):
    cv.save(); cv.translate(x, y); cv.scale(s, s)
    pal = P("#070B16")
    cv.drawRect(skia.Rect.MakeXYWH(-150, -110, 300, 110), pal); cv.drawRect(skia.Rect.MakeXYWH(-60, -170, 120, 170), pal)
    cv.drawOval(skia.Rect.MakeXYWH(-50, -225, 100, 90), pal)
    for bx in (-150, 110):
        cv.drawRect(skia.Rect.MakeXYWH(bx, -160, 40, 160), pal); cv.drawOval(skia.Rect.MakeXYWH(bx - 3, -185, 46, 46), pal)
    rim = P("#E2B661", 70, 3)
    cv.drawRect(skia.Rect.MakeXYWH(-150, -110, 300, 110), rim); cv.drawRect(skia.Rect.MakeXYWH(-60, -170, 120, 60), rim)
    cv.drawOval(skia.Rect.MakeXYWH(-50, -225, 100, 90), rim)
    for k in range(6):
        cv.drawRect(skia.Rect.MakeXYWH(-130 + k * 48, -80, 18, 30), P("#E7BD6A", 110 + 60 * math.sin(t * 3 + k)))
    if fire > 0:
        cv.drawCircle(0, -120, 300, rad((0, -120), 300, [("#FF7A2A", 120 * fire), ("#FF7A2A", 0)]))
        for k in range(7):
            fx = -120 + k * 40; fh = 60 + 50 * math.sin(t * 9 + k * 1.7)
            fl = skia.Path(); fl.moveTo(fx - 22, -110); fl.quadTo(fx, -110 - fh * 1.6 * fire, fx + 22, -110); fl.close()
            cv.drawPath(fl, lin((0, -110 - fh * 1.6), (0, -110), [("#FFE08A", 230 * fire), ("#FF6A2A", 230 * fire)]))
    cv.restore()

def ship(cv, x, y, s, t=0.):
    cv.save(); cv.translate(x, y); cv.scale(s, s)
    body, rim = "#26324F", "#E2B661"
    hull = skia.Path(); hull.moveTo(-160, 0); hull.lineTo(150, 0); hull.lineTo(120, 44); hull.lineTo(-130, 44); hull.close()
    cv.drawPath(hull, P(body)); cv.drawPath(hull, P(rim, 140, 3))
    cv.drawRect(skia.Rect.MakeXYWH(-80, -34, 150, 34), P(body)); cv.drawRect(skia.Rect.MakeXYWH(-80, -34, 150, 34), P(rim, 115, 3))
    for fx in (-40, 15):
        cv.drawRect(skia.Rect.MakeXYWH(fx, -84, 22, 50), P(body)); cv.drawRect(skia.Rect.MakeXYWH(fx, -84, 22, 8), P("#B23A2E"))
    cv.drawLine(-115, 0, -115, -125, P(body, 255, 6)); cv.drawLine(95, 0, 95, -110, P(body, 255, 6))
    for k in range(6): cv.drawCircle(-110 + k * 42, 20, 6, P("#FFD27A", 150 + 100 * math.sin(t * 4 + k)))
    for k in range(3): cv.drawCircle(-30 + k * 18 + 10 * math.sin(t + k), -100 - k * 26, 14 + k * 6, P("#6E7790", 90 - 20 * k))
    cv.restore()

def ink_blot(cv, cx, cy, r, t):
    if r <= 1: return
    pth = skia.Path()
    for k in range(97):
        an = 2 * math.pi * k / 96
        rr = r * (1 + .07 * math.sin(7 * an + t * 9) + .05 * math.sin(13 * an - t * 6))
        (pth.moveTo if k == 0 else pth.lineTo)(cx + rr * math.cos(an), cy + rr * math.sin(an))
    pth.close(); cv.drawPath(pth, P("#05080F")); cv.drawPath(pth, P("#D6A650", 200, 6))
    for k in range(10):
        an = k * 36 + 11; d = r * (1.08 + .12 * math.sin(k * 3.3))
        cv.drawCircle(cx + d * math.cos(math.radians(an)), cy + d * math.sin(math.radians(an)), r * .035 + 4, P("#05080F"))

def thumb(cv, x, y, s):
    cv.save(); cv.translate(x, y); cv.scale(s, s)
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-90, -20, 40, 120), 10, 10), P("#F1E4C4"))
    hd = skia.Path(); hd.moveTo(-40, -10); hd.lineTo(-10, -70); hd.quadTo(5, -120, 25, -105); hd.quadTo(40, -90, 20, -30)
    hd.lineTo(75, -30); hd.quadTo(100, -28, 92, 0); hd.lineTo(80, 80); hd.quadTo(74, 100, 50, 100); hd.lineTo(-40, 100); hd.close()
    cv.drawPath(hd, P("#F1E4C4")); cv.drawPath(hd, P("#3A2410", 255, 6))
    cv.restore()

def strike(cv, x0, x1, y, k):
    if k <= 0: return
    cv.drawLine(x0, y, x0 + (x1 - x0) * k, y - 6, P("#D23A2E", 255, 10))

# =================================================================== SCENES
# each returns owl hints: look, surprise, mood, point, pose
def sc_hook(cv, p, lt, dur, si, t):
    rays(cv, W / 2, 430, t, 26)
    watch(cv, W / 2, 430, 170 * eback(lt / .5), lt * 80, lt * 460, lt * 1100, glow=.5)
    n = int(round(38 * eo((lt - .1) / .7)))
    t_j, t_h, t_m = word_time(si, "jours"), word_time(si, "heures"), word_time(si, p.get("slam_on", "minutes#2"))
    punch = 1.0; flash = 0; shake = 0
    if t_m is not None and t >= t_m:
        k = t - t_m; punch = 1 + .16 * math.exp(-k * 8); flash = math.exp(-k * 8); shake = 14 * math.exp(-k * 7) * math.sin(k * 60)
    cv.save(); cv.translate(shake, 0)
    cv.save(); cv.translate(W / 2, 760); s = (.75 + .25 * eback(lt / .35)) * punch; cv.scale(s, s)
    gold(cv, f"{n} MINUTES", 0, 0, fit("88 MINUTES", "title", 140, W * .76)); cv.restore()
    for (tw, label, y) in ((t_j, "PAS 38 JOURS", 885), (t_h, "PAS 38 HEURES", 975)):
        if tw is not None and t >= tw - .25:
            k = eo((t - tw + .25) / .3)
            f = font("title", 62); w = f.measureText(label)
            text_c(cv, label, W / 2, y, f, "#F1E4C4", 255 * k)
            strike(cv, W / 2 - w / 2 - 14, W / 2 + w / 2 + 14, y - 20, eo((t - tw - .25) / .25))
    cv.restore()
    if flash > .01: cv.drawRect(skia.Rect.MakeWH(W, H), P("#FFE2A8", 90 * flash))
    return dict(surprise=clamp(1 - lt / .8) + flash * .6, mood="surprised" if lt < 1 else "neutral", look=(0, -1))

def sc_place(cv, p, lt, dur, si, t):
    compass(cv, W / 2, 470, 230, lt * 14, 180 * clamp(lt / .4))
    isl = skia.Path(); isl.moveTo(300, 745); isl.cubicTo(380, 688, 700, 688, 780, 745); isl.close()
    cv.drawPath(isl, P("#070B16")); palm(cv, 420, 730, .8, t); palm(cv, 650, 735, .65, t + 1)
    waves(cv, 735, 805, t, 3, 9)
    d = ebounce((lt - .15) / .8); pin(cv, W / 2, -150 + 855 * d, .9)
    name = p.get("big", ""); ns = int(len(name) * clamp((lt - .55) / .8))
    if ns:
        sz = fit(name, "title", 150, W * .86); fw = font("title", sz).measureText(name); part = name[:ns]
        gold(cv, part, W / 2 - fw / 2 + font("title", sz).measureText(part) / 2, 920, sz)
    if p.get("small") and lt > 1.3:
        k = eback((lt - 1.3) / .35)
        cv.save(); cv.translate(W / 2, 1010); cv.rotate(-7); cv.scale(2 - k, 2 - k)
        f = font("title", 48); w = f.measureText(p["small"]); a = 255 * clamp((lt - 1.3) / .2)
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 - 30, -56, w + 60, 78), 12, 12), P("#C0392B", a, 6))
        cv.drawString(p["small"], -w / 2, 0, f, P("#E25A47", a)); cv.restore()
    return dict(mood="neutral", look=(-.7, -.6))

def sc_scroll(cv, p, lt, dur, si, t):
    cx, cy, wd = W / 2 + 60, 540, 700
    hg = 560 * eo((lt - .1) / .7)
    cv.drawRect(skia.Rect.MakeXYWH(cx - wd / 2, cy - hg / 2, wd, hg), lin((0, cy - hg / 2), (0, cy + hg / 2), ["#F0DFB4", "#E2CB94"]))
    cv.drawRect(skia.Rect.MakeXYWH(cx - wd / 2, cy - hg / 2, wd, hg), lin((cx - wd / 2, 0), (cx + wd / 2, 0),
                [("#8A6A3A", 110), ("#8A6A3A", 0), ("#8A6A3A", 0), ("#8A6A3A", 110)], [0, .15, .85, 1]))
    for yy in (cy - hg / 2, cy + hg / 2):
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - wd / 2 - 30, yy - 26, wd + 60, 52), 26, 26)
        cv.drawRRect(rr, lin((0, yy - 26), (0, yy + 26), ["#E0C285", "#9E7A42"])); cv.drawRRect(rr, P("#6E4E22", 255, 4))
    a = 255 * clamp((lt - .6) / .3)
    if hg > 300:
        t1 = p.get("big", ""); text_c(cv, t1, cx, cy - 30, font("title", fit(t1, "title", 104, wd - 80)), "#4A2E14", a, False)
        cv.drawLine(cx - 180, cy + 10, cx + 180, cy + 10, P("#7A5426", a, 3))
        if p.get("line"): text_c(cv, p["line"], cx, cy + 80, font("sub", fit(p["line"], "sub", 52, wd - 90)), "#4A2E14", a, False)
    ts = word_time(si, p.get("seal_on"))
    if ts is not None and t >= ts:
        k = eo((t - ts) / .22); sc = 2.4 - 1.4 * k
        cv.save(); cv.translate(cx + 230, cy + hg / 2 - 90); cv.scale(sc, sc)
        cv.drawCircle(0, 0, 66, rad((-15, -15), 90, [("#C23A30", 255 * k), ("#7E1E16", 255 * k)]))
        cv.drawCircle(0, 0, 52, P("#6E1A14", 255 * k, 5)); text_c(cv, "E", 0, 22, font("title", 62), "#E77B6C", 255 * k, False)
        cv.restore()
    if p.get("pill") and lt > 1.0:
        k = eback((lt - 1.0) / .4)
        cv.save(); cv.translate(cx, 975); cv.scale(k, k)
        f = font("title", 46); w = f.measureText(p["pill"])
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 - 80, -50, w + 120, 70), 35, 35)
        cv.drawRRect(rr, P("#0B1224", 230)); cv.drawRRect(rr, P("#D6A650", 255, 3))
        cv.drawCircle(-w / 2 - 40, -15, 20, P("#D6A650", 255, 3)); cv.drawLine(-w / 2 - 40, -15, -w / 2 - 40, -28, P("#D6A650", 255, 3))
        cv.drawLine(-w / 2 - 40, -15, -w / 2 - 30, -15, P("#D6A650", 255, 3)); cv.drawString(p["pill"], -w / 2 + 10, 2, f, P("#F0CF85"))
        cv.restore()
    return dict(mood="worried", look=(.8, -.6))

def sc_battle(cv, p, lt, dur, si, t):
    hz = 720
    a = 255 * clamp(lt / .3)
    hh, mm = [int(v) for v in p.get("time", "9:02").split(":")]
    watch(cv, 250, 330, 85, (hh % 12 + mm / 60) * 30, mm * 6, lt * 360, a=a)
    cv.save(); cv.translate(660, 380); k0 = eback(lt / .4); cv.scale(k0, k0)
    gold(cv, p.get("big", ""), 0, 0, fit(p.get("big", ""), "title", 140, 560), a); cv.restore()
    if p.get("small"): text_c(cv, p["small"], 660, 450, font("sub", 46), "#F1E4C4", a * clamp((lt - .4) / .4))
    tf = word_time(si, p.get("shake_on")); tk = word_time(si, p.get("sink_on"))
    shots = [tf + k * .3 for k in range(3)] if tf is not None else []
    shake = 0; flash = 0
    for s_ in shots:
        if t >= s_: k = t - s_; shake += 14 * math.exp(-k * 6) * math.sin(k * 70); flash = max(flash, math.exp(-k * 8))
    cv.save(); cv.translate(shake, shake * .5)
    cv.drawRect(skia.Rect.MakeXYWH(0, hz - 240, W, 240), lin((0, hz - 240), (0, hz), [("#E07A3A", 0), ("#E07A3A", 95)]))
    fire = clamp((t - shots[0] - .3) / 1.2) if shots else 0
    palace(cv, 230, hz + 4, .9, fire, t)
    for i, s_ in enumerate(shots):
        q = (t - s_) / .55
        if 0 <= q <= 1:
            sx, sy, ex, ey = 780 - i * 125, hz + 30, 260, hz - 80
            x = sx + (ex - sx) * q; y = sy + (ey - sy) * q - 180 * math.sin(math.pi * q)
            cv.drawCircle(x, y, 22, P("#FFD27A", 60)); cv.drawCircle(x, y, 9, P("#FFF0C0"))
        if 1 <= q <= 1.9:
            r = 40 + 130 * (q - 1); cv.drawCircle(260, hz - 80, r, P("#FFB04A", 200 * (1.9 - q) / .9))
    waves(cv, hz + 10, hz + 90, t, 2, 10)
    for i in range(3):
        sx = W + 260 - (W * .62 - i * 125 + 260) * eo((lt - .1 - .15 * i) / 1.0)
        ship(cv, sx, hz + 40 + 34 * i + 5 * math.sin(t * 2 + i), .74 + .13 * i, t)
        if i < len(shots) and t >= shots[i]:
            kk = t - shots[i]
            cv.drawCircle(sx - 150, hz + 30 + 26 * i, 42 * math.exp(-kk * 5) + 2, P("#FFE08A", 255 * math.exp(-kk * 4)))
            for j in range(5):
                cv.drawCircle(sx - 130 - kk * 40 - j * 12, hz + 60 + 26 * i - kk * 50 - j * 10, 16 + kk * 46 + j * 8, P("#9AA3B5", 110 * math.exp(-kk * 1.1)))
    ys = eo((t - tk) / 1.4) if tk is not None and t >= tk else 0
    cv.save(); cv.translate(430, hz + 70 + 70 * ys); cv.rotate(-25 * ys)
    hl = skia.Path(); hl.moveTo(-60, 0); hl.lineTo(60, 0); hl.lineTo(45, 20); hl.lineTo(-48, 20); hl.close()
    cv.drawPath(hl, P("#F1E4C4", 255 * (1 - ys))); cv.drawLine(0, 0, 0, -60, P("#F1E4C4", 255 * (1 - ys), 4)); cv.restore()
    waves(cv, hz + 150, hz + 330, t + 3, 4, 13)
    for j in range(16):   # fire / sunset reflections on the water
        yy = hz + 30 + j * 16; ww = 120 + 60 * math.sin(t * 2 + j)
        cv.drawRect(skia.Rect.MakeXYWH(230 - ww / 2 + 20 * math.sin(t * 3 + j * 1.3), yy, ww, 3),
                    P("#FFB04A", (40 + 120 * fire) * (1 - j / 16)))
    cv.restore()
    if flash > .01: cv.drawRect(skia.Rect.MakeWH(W, H), P("#FFB86B", 70 * flash))
    return dict(mood="surprised" if flash > .2 else "serious", surprise=clamp(flash * 1.3), look=(.9, -.4), point=1.0)

def sc_toll(cv, p, lt, dur, si, t):
    # sober scene: smoking palace, falling flag, casualty figures
    cv.drawRect(skia.Rect.MakeXYWH(0, 300, W, 420), lin((0, 300), (0, 720), [("#E07A3A", 0), ("#E07A3A", 55)]))
    palace(cv, W / 2, 690, 1.25, .35 + .15 * math.sin(t * 2), t)
    for j in range(8):
        k = (t * .25 + j / 8) % 1
        cv.drawCircle(W / 2 - 80 + 30 * math.sin(j * 2.1 + t * .5), 520 - 380 * k, 30 + 70 * k, P("#4A5166", 120 * (1 - k)))
    tf = word_time(si, p.get("flag_on"))
    k = eo((t - tf) / 1.0) if tf is not None and t >= tf else 0
    px, top = W / 2, 300
    cv.drawLine(px, top, px, 410, P("#C9A56A", 255, 9)); cv.drawCircle(px, top, 11, P("#E2B661"))
    cv.save(); cv.translate(px, top + 10 + 140 * k); cv.rotate(50 * k)
    fl = skia.Path(); fl.moveTo(0, 0)
    for i in range(0, 201, 10): fl.lineTo(i, 10 * math.sin(i / 30 - t * 6) * (i / 200))
    for i in range(200, -1, -10): fl.lineTo(i, 120 + 10 * math.sin(i / 30 - t * 6) * (i / 200))
    fl.close(); cv.drawPath(fl, P("#B23A2E", 255 * (1 - k))); cv.restore()
    tl, tr = word_time(si, p.get("left_on")), word_time(si, p.get("right_on"))
    y = 880
    if tl is not None and t >= tl:
        q = t - tl; nv = int(round(p["left"] * eo(q / 1.3)))
        a = 255 * clamp(q / .4)
        text_c(cv, f"~{nv}", 300, y, font("title", 140), "#D9806A", a)
        text_c(cv, p.get("left_label", ""), 300, y + 64, font("sub", 40), "#F1E4C4", a)
        text_c(cv, "contre", W / 2 + 20, y - 40, font("sub", 46), "#D6A650", a)
    if tr is not None and t >= tr:
        q = t - tr; a = 255 * clamp(q / .4)
        cv.save(); cv.translate(800, y); s = .8 + .2 * eo(q / .4); cv.scale(s, s)
        text_c(cv, str(p["right"]), 0, 0, font("title", 140), "#E9D9B4", a)
        text_c(cv, p.get("right_label", ""), 0, 64, font("sub", 40), "#F1E4C4", a); cv.restore()
    return dict(mood="serious", look=(-.6, -.6))

def sc_finale(cv, p, lt, dur, si, t):
    rays(cv, W / 2, 470, t, 22)
    watch(cv, W / 2, 470, 175, lt * 80, lt * 900, lt * 2000, glow=.8 + .2 * math.sin(t * 8))
    txt = p.get("big", ""); n_ = int(len(txt) * clamp((lt - .6) / 1.0))
    if p.get("small"): text_c(cv, p["small"], W / 2, 745, font("sub", 56), "#F1E4C4", 255 * clamp(lt / .5))
    if n_:
        sz = fit(txt, "title", 130, W * .84); fw = font("title", sz).measureText(txt); part = txt[:n_]
        gold(cv, part, W / 2 - fw / 2 + font("title", sz).measureText(part) / 2, 910, sz)
    return dict(mood="neutral", look=(0, -1))

def sc_cta(cv, p, lt, dur, si, t):
    rays(cv, W / 2, 560, t, 20)
    a = 255 * clamp(lt / .3)
    text_c(cv, p.get("big", "TU AS AIMÉ ?"), W / 2, 330, font("title", 84), "#F4D692", a)
    tl = word_time(si, p.get("like_on", "laisse"))
    popk = 1 + .35 * math.exp(-(t - tl) * 6) if tl is not None and t >= tl else 1
    thumb(cv, W / 2, 560, 1.25 * eback(lt / .45) * popk + .04 * math.sin(t * 5))
    if tl is not None and t >= tl:
        for j in range(10):
            an = j * 36 + 20; r = 140 + 120 * clamp((t - tl) / .6)
            cv.drawCircle(W / 2 + r * math.cos(math.radians(an)), 560 + r * math.sin(math.radians(an)), 9, P("#F6C85A", 255 * (1 - clamp((t - tl) / .8))))
    ts = word_time(si, p.get("sub_on", "abonne")); tap = ts + .7 if ts is not None else 9e9
    pressed = t >= tap; pulse = 1 + .05 * math.sin(t * 8) if not pressed else 1
    cv.save(); cv.translate(W / 2, 820); kb = eback(lt / .45); cv.scale(kb * pulse, kb * pulse)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-300, -66, 600, 132), 66, 66)
    cv.drawRRect(rr, P("#3A3F4A" if pressed else "#D62B2B"))
    lab = "ABONNÉ" if pressed else "S'ABONNER"; f = font("cap", 62); w = f.measureText(lab)
    cv.drawString(lab, -w / 2 + 30, 22, f, P("#FFFFFF"))
    bx = -w / 2 - 34; bl = skia.Path(); bl.moveTo(bx - 26, 18); bl.quadTo(bx - 24, -34, bx, -34); bl.quadTo(bx + 24, -34, bx + 26, 18); bl.close()
    cv.drawPath(bl, P("#FFFFFF")); cv.drawCircle(bx, 26, 8, P("#FFFFFF")); cv.restore()
    if pressed:
        q = t - tap; cv.drawCircle(W / 2 + 150, 840, 30 + 160 * q, P("#FFFFFF", 160 * clamp(1 - q / .5), 6))
    return dict(mood="happy", look=(0, -1), point=.65 + .35 * math.sin(t * 9))

def sc_throne(cv, p, lt, dur, si, t):
    cx = W / 2 - 60
    rays(cv, cx, 520, t, 18)
    # throne silhouette with gold rim
    th = skia.Path()
    th.moveTo(cx - 150, 760); th.lineTo(cx - 150, 520); th.quadTo(cx - 150, 330, cx, 300)
    th.quadTo(cx + 150, 330, cx + 150, 520); th.lineTo(cx + 150, 760); th.close()
    cv.drawPath(th, lin((0, 300), (0, 760), ["#3A1E2E", "#1A0E16"])); cv.drawPath(th, P("#E2B661", 200, 6))
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 210, 600, 420, 70), 18, 18), lin((0, 600), (0, 670), ["#6E2A3A", "#3A1420"]))
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - 210, 600, 420, 70), 18, 18), P("#E2B661", 200, 5))
    for k in (-1, 1):
        cv.drawRect(skia.Rect.MakeXYWH(cx + k * 190 - 18, 520, 36, 240), P("#2A1420")); cv.drawCircle(cx + k * 190, 515, 26, P("#E2B661"))
    # crown falls onto the throne
    tc = word_time(si, p.get("crown_on")) or (seg_bounds[si][0] + .4)
    k = ebounce((t - tc) / .8) if t >= tc else 0
    cy_ = -200 + (560 + 200) * k
    cv.save(); cv.translate(cx, cy_); cv.scale(1.2, 1.2)
    cr = skia.Path(); cr.moveTo(-110, 0)
    for i, x in enumerate([-110, -70, -35, 0, 35, 70, 110]): cr.lineTo(x, -110 if i % 2 == 0 else -50)
    cr.lineTo(110, 0); cr.close()
    cv.drawPath(cr, lin((0, -110), (0, 0), ["#FCE9B6", "#C48D3C"])); cv.drawPath(cr, P("#7A4E1C", 255, 4))
    for x in (-70, 0, 70): cv.drawCircle(x, -30, 12, P("#B23A2E"))
    cv.restore()
    if t >= tc + .5:
        q = t - tc - .5
        sz = fit(p.get("big", ""), "title", 140, W * .8)
        gold(cv, p.get("big", ""), W / 2, 900, sz, 255 * clamp(q / .3))
        if p.get("small"): text_c(cv, p["small"], W / 2, 975, font("sub", 52), "#F1E4C4", 255 * clamp((q - .2) / .3))
    te = word_time(si, p.get("stamp_on"))
    surprise = 0
    if te is not None and t >= te:
        q = t - te; kk = eo(q / .2); sc = 2.2 - 1.2 * kk
        cv.save(); cv.translate(W / 2, 560); cv.rotate(-12); cv.scale(sc, sc)
        lab = p.get("stamp", "GROSSE ERREUR"); f = font("title", 92); w = f.measureText(lab)
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 - 40, -100, w + 80, 132), 16, 16)
        cv.drawRRect(rr, P("#1A0608", 150 * kk)); cv.drawRRect(rr, P("#E0402F", 255 * kk, 10))
        cv.drawString(lab, -w / 2, 0, f, P("#F05A45", 255 * kk)); cv.restore()
        surprise = clamp(1 - q / .8)
    return dict(mood="surprised" if surprise > .3 else "worried", surprise=surprise * .8, look=(-.7, -.6))

SCENES = dict(hook=sc_hook, place=sc_place, scroll=sc_scroll, battle=sc_battle, toll=sc_toll, finale=sc_finale, cta=sc_cta, throne=sc_throne)
SFX_HOOKS = []
# scene packs: extra scene files that register new scenes / sound hooks
for _pack in spec.get("scene_packs", []):
    _pp = _pack if os.path.isabs(_pack) else os.path.join(os.path.dirname(os.path.abspath(__file__)), _pack)
    exec(compile(open(_pp).read(), _pp, "exec"), globals())

# =================================================================== SCENE SFX
for si, seg in enumerate(SEGS):
    p = seg["scene"]; a_, b_ = seg_bounds[si]; ty = p["type"]
    if si > 0: put(music, taiko(), a_ - .05, .35)
    if ty == "hook":
        for k in np.arange(0, .8, .06): put(sfx, tick(), a_ + .1 + k, .25)
        for key in ("jours", "heures"):
            tw = word_time(si, key); tw is not None and put(sfx, thud(), tw + .25, .5)
        tm = word_time(si, p.get("slam_on", "minutes#2")); tm is not None and put(sfx, boom(), tm, .9)
    if ty == "place": put(sfx, pop(), a_ + .15 + .8 * .36, .4)
    if ty == "scroll":
        put(sfx, whoosh(.7), a_ + .1, .25)
        ts = word_time(si, p.get("seal_on")); ts is not None and put(sfx, thud(), ts + .15, .8)
    if ty == "battle":
        tf = word_time(si, p.get("shake_on"))
        if tf is not None:
            put(music, riser(1.8), tf - 1.8, .35)
            for k in range(3): put(sfx, boom(), tf + .3 * k, .8, pan=(-.4 + .4 * k))
        tk = word_time(si, p.get("sink_on")); tk is not None and put(sfx, splash(), tk + .3, .5)
    if ty == "toll":
        tf = word_time(si, p.get("flag_on")); tf is not None and put(sfx, whoosh(.9), tf, .25)
        tl = word_time(si, p.get("left_on")); tl is not None and put(music, taiko(1.5, 55), tl, .5)
    if ty == "throne":
        tc = word_time(si, p.get("crown_on")) or (a_ + .4); put(sfx, pop(), tc + .8 * .36, .5); put(sfx, tick(), tc + .8, .6)
        te = word_time(si, p.get("stamp_on")); te is not None and (put(sfx, thud(), te + .15, .9), put(music, taiko(1.2, 60), te + .12, .5))
    if ty == "finale":
        for k in np.arange(0, b_ - a_, .5): put(sfx, tick(), a_ + k, .35)
    for _hook in SFX_HOOKS: _hook(si, seg, p, a_, b_, ty)
    if ty == "cta":
        motif(a_ + .1, .2)
        ts = word_time(si, p.get("sub_on", "abonne")); ts is not None and put(sfx, pop(), ts + .7, .55)
        tl = word_time(si, p.get("like_on", "laisse")); tl is not None and put(sfx, pop(), tl, .45)

# =================================================================== MIX
sf.write(f"{work}/voice_raw.wav", voice, vsr)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{work}/voice_raw.wav", "-af",
                "aresample=44100,highpass=f=75,equalizer=f=260:t=q:w=1:g=-2.5,equalizer=f=3200:t=q:w=1.2:g=3.5,"
                "deesser=i=0.4,acompressor=threshold=-20dB:ratio=3:attack=5:release=120:makeup=2.5"
                + ("" if spec.get("narration") else ",aecho=0.9:0.5:28:0.05"), "-ac", "1", f"{work}/voice_fx.wav"], check=True)
vfx, _ = sf.read(f"{work}/voice_fx.wav")
vfx = np.pad(vfx, (0, max(0, N - len(vfx))))[:N]
wet = np.stack([signal.fftconvolve(music[:, c] + .6 * sfx[:, c], ir)[:N] for c in range(2)], axis=1)
bus = music * .8 + sfx + wet * .35
venv = np.abs(vfx); venv = signal.sosfilt(signal.butter(1, 6, "low", fs=SR, output="sos"), venv)
venv = np.clip(venv / (np.percentile(venv, 98) + 1e-9), 0, 1)
bus *= (1 - .55 * venv)[:, None]
mix = bus * .9 + np.stack([vfx, vfx], axis=1) * 1.0
mix = np.tanh(mix * 1.05)
sf.write(f"{work}/mix.wav", mix[:int(TOTAL * SR)].astype(np.float32), SR)

# =================================================================== OWL CHOREOGRAPHY
OWL = [seg.get("owl", {}) for seg in SEGS]
COSTUME = spec.get("costume", {})
random.seed(11); BLINKS = []; b0 = .9
while b0 < TOTAL: BLINKS.append(b0); b0 += random.uniform(2.4, 4.4)
HOP = .45

def owl_state(t):
    si = next((i for i, (a, b) in enumerate(seg_bounds) if a <= t < b), len(SEGS) - 1)
    cur = OWL[si]; x, face, sc = cur.get("x", 540), cur.get("face", 1), cur.get("scale", .58)
    y_off = 0; squash = 0
    if si + 1 < len(SEGS):
        nb = seg_bounds[si][1]
        if t > nb - HOP:
            q = (t - (nb - HOP)) / HOP; nx = OWL[si + 1].get("x", 540)
            x = x + (nx - x) * eio(q); y_off = -70 * math.sin(math.pi * q)
            sc = sc + (OWL[si + 1].get("scale", .58) - sc) * eio(q)
            if q > .5: face = OWL[si + 1].get("face", 1)
    if si > 0:
        dl = t - seg_bounds[si][0]
        if 0 <= dl < .25: squash = math.sin(math.pi * dl / .25) * .12
    return x, face, sc, y_off, squash, si

def draw_owl_at(cv, t, f, hints):
    x, face, sc, y_off, squash, si = owl_state(t)
    e = float(ENV[min(f, NF - 1)])
    blink = 0.
    for b in BLINKS:
        d = t - b
        if 0 <= d < .16: blink = 1 - abs(d - .08) / .08
    bob = 6 * math.sin(t * 2.4)
    lk = hints.get("look", (0, -1)); lk = (lk[0] * face, lk[1])
    cv.save(); cv.translate(x, 1700 + y_off + bob)
    cv.scale(sc * face * (1 + squash), sc * (1 - squash + .035 * e))
    draw_owl(cv, t, e=e, costume=COSTUME, look=lk, surprise=hints.get("surprise", 0), blink=blink,
             point=hints.get("point", GEST[min(f, NF - 1)]), mood=hints.get("mood", "neutral"))
    cv.restore()

# =================================================================== CAPTIONS
def captions(cv, t):
    ch = None
    for c in chunks:
        if c["t0"] - .05 <= t < c["t1"] + .12: ch = c
    if not ch: return
    f = font("cap", 66); toks = [words[i]["text"] for i in ch["w"]]
    ws = [f.measureText(w) for w in toks]; sp = (f.measureText("a a") - f.measureText("aa")) * 1.7
    tw = sum(ws) + sp * (len(toks) - 1); scale = min(1., (W - 120) / tw)
    pop_ = eback((t - ch["t0"]) / .18)
    cv.save(); cv.translate(W / 2, 1150); cv.scale(scale * (.85 + .15 * pop_), scale * (.85 + .15 * pop_))
    x = -tw / 2
    for i, wi in enumerate(ch["w"]):
        w = words[wi]; act = w["t0"] <= t < w["t1"] + .05
        cv.save()
        if act: cv.translate(0, -6)
        cv.drawString(toks[i], x, 0, f, P("#000000", 255, 10))
        cv.drawString(toks[i], x, 0, f, P("#F6C85A" if act else "#FFFFFF"))
        cv.restore(); x += ws[i] + sp
    cv.restore()

# =================================================================== RENDER
surface = skia.Surface(W, H)
info = skia.ImageInfo.Make(W, H, skia.kRGBA_8888_ColorType, skia.kPremul_AlphaType)
buf = np.zeros((H, W, 4), np.uint8)
PREVIEW = os.environ.get("PREVIEW")
frames = [int(float(x) * FPS) for x in PREVIEW.split(",")] if PREVIEW else range(NF)
ff = None
if not PREVIEW:
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-i", f"{work}/mix.wav",
                           "-af", "loudnorm=I=-14:TP=-1.5:LRA=11",
                           "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p",
                           "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-shortest", "-movflags", "+faststart", out_path],
                          stdin=subprocess.PIPE)
TR = .24
for f in frames:
    t = f / FPS
    cv = surface.getCanvas()
    si = next((i for i, (a, b) in enumerate(seg_bounds) if a <= t < b), len(SEGS) - 1)
    a, b = seg_bounds[si]; seg = SEGS[si]; lt = t - a
    background(cv, t, warm=seg.get("tension", .4))
    # gentle camera push-in per scene
    z = 1 + .045 * eio(lt / max(.1, b - a))
    cv.save(); cv.translate(W / 2, 620); cv.scale(z, z); cv.translate(-W / 2, -620)
    hints = SCENES[seg["scene"]["type"]](cv, seg["scene"], lt, b - a, si, t) or {}
    cv.restore()
    for (bb, _) in seg_bounds[1:]:
        d = abs(t - bb)
        if d < TR: ink_blot(cv, W / 2, 620, 1300 * eo(1 - d / TR), t)
    foreground(cv, t, f)
    header(cv, t)
    draw_owl_at(cv, t, f, hints)
    captions(cv, t)
    surface.readPixels(info, buf, W * 4)
    if PREVIEW:
        from PIL import Image
        Image.fromarray(buf[:, :, :3].copy()).resize((540, 960)).save(f"{work}/prev_{t:05.1f}.png"); continue
    ff.stdin.write(buf.tobytes())
if ff:
    ff.stdin.close(); ff.wait()
print(json.dumps({"duration": round(TOTAL, 2), "frames": NF, "out": out_path}))
