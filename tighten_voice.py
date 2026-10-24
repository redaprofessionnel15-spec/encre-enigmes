"""Shorten long pauses in a narration and speed it up slightly.

python3 tighten_voice.py in.mp3 out.wav [tempo=1.06] [keep=0.30] [ratio=0.28]
Pauses longer than `keep` seconds are shortened to keep + (extra * ratio).
"""
import subprocess, sys, os, tempfile
import numpy as np
import soundfile as sf

src, dst = sys.argv[1], sys.argv[2]
tempo = float(sys.argv[3]) if len(sys.argv) > 3 else 1.06
KEEP = float(sys.argv[4]) if len(sys.argv) > 4 else 0.30
RATIO = float(sys.argv[5]) if len(sys.argv) > 5 else 0.28

tmp = tempfile.mkdtemp()
raw = os.path.join(tmp, "raw.wav")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", "24000", raw], check=True)
x, sr = sf.read(raw)
hop = int(.01 * sr)
rms = np.array([np.sqrt(np.mean(x[i:i + hop] ** 2)) for i in range(0, len(x) - hop, hop)])
thr = np.percentile(rms[rms > 1e-4], 90) * 0.06
sil = rms < thr
out, pos, i = [], 0, 0
while i < len(sil):
    if sil[i]:
        j = i
        while j < len(sil) and sil[j]:
            j += 1
        d = (j - i) * .01
        if d >= .12:
            keep = d if d <= KEEP else KEEP + (d - KEEP) * RATIO
            a, b = i * hop, j * hop
            half = int(keep * sr / 2)
            out += [x[pos:a], x[a:a + half], x[b - half:b]]
            pos = b
        i = j
    else:
        i += 1
out.append(x[pos:])
y = np.concatenate(out)
idx = np.where(np.abs(y) > 0.01)[0]
y = y[max(0, idx[0] - int(.1 * sr)): idx[-1] + int(.25 * sr)]
tight = os.path.join(tmp, "tight.wav")
sf.write(tight, y, sr)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tight, "-af", f"atempo={tempo}", dst], check=True)
z, _ = sf.read(dst)
print(f"{len(x) / sr:.2f}s -> {len(z) / sr:.2f}s")
