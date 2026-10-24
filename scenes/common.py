# Scene pack: generic scenes reusable in any episode (always loaded by engine.py)
#
#   counter : {"value": 29, "unit": "ANS", "label": "de guerre en trop", "from": 0, "slam_on": "29"}
#   year    : {"year": 1932, "from": 2026, "place": "AUSTRALIE", "land_on": "1932"}
#   versus  : {"left": 20000, "left_label": "émeus", "right": 986, "right_label": "abattus", "left_on": "..", "right_on": ".."}
#   verdict : {"claim": "Napoléon était petit", "stamp": "FAUX", "stamp_on": "faux"}   (stamp "VRAI" turns green)
#   quote   : {"title": "ORDRE DU JOUR", "sign": "— Major Meredith"}   (the segment's narration is written by a quill)

def _k_on(si, key, t, dur=.3):
    tw = word_time(si, key) if key else None
    return (tw, clamp((t - tw) / dur)) if tw is not None and t >= tw else (tw, 0.)

def _shake(t0, t, amp=16):
    if t0 is None or t < t0: return 0.
    k = t - t0; return amp * math.exp(-k * 7) * math.sin(k * 60)

def _num(n):
    return f"{n:,}".replace(",", " ")   # Cinzel has no narrow no-break space

def sc_counter(cv, p, lt, dur, si, t):
    rays(cv, W / 2, 620, t, 24)
    v0, v1 = p.get("from", 0), p["value"]
    ts, _ = _k_on(si, p.get("slam_on"), t)
    end = (ts - seg_bounds[si][0]) if ts is not None else min(1.4, dur * .5)
    n = int(round(v0 + (v1 - v0) * eo(lt / max(.2, end))))
    punch = 1 + (.18 * math.exp(-(t - ts) * 8) if ts is not None and t >= ts else 0)
    cv.save(); cv.translate(_shake(ts, t), 0)
    cv.save(); cv.translate(W / 2, 660); cv.scale(punch * (.7 + .3 * eback(lt / .3)), punch * (.7 + .3 * eback(lt / .3)))
    txt = _num(n); gold(cv, txt, 0, 0, fit(_num(v1), "title", 300, W * .8))
    cv.restore()
    if p.get("unit"): gold(cv, p["unit"], W / 2, 800, fit(p["unit"], "title", 110, W * .8), 255 * clamp(lt / .3))
    if p.get("label"): text_c(cv, p["label"], W / 2, 880, font("sub", 58), "#F1E4C4", 255 * clamp((lt - .3) / .4))
    cv.restore()
    if ts is not None and t >= ts:
        cv.drawRect(skia.Rect.MakeWH(W, H), P("#FFE2A8", 90 * math.exp(-(t - ts) * 8)))
        return dict(mood="shocked" if t - ts < .8 else "surprised", surprise=clamp(1 - (t - ts) / .8), look=(0, -1))
    return dict(mood="curious", look=(0, -1))

def sc_year(cv, p, lt, dur, si, t):
    y0, y1 = p.get("from", 2026), p["year"]
    tl, _ = _k_on(si, p.get("land_on"), t)
    end = max(1.0, (tl - seg_bounds[si][0]) if tl is not None else min(1.6, dur * .6))   # always spin >= 1 s
    k = eio(lt / end); yr = int(round(y0 + (y1 - y0) * k))
    spin = (1 - k) * 24
    for r in range(5):   # time tunnel rings
        rr = ((t * 260 * (1 - k * .8) + r * 160) % 800) + 40
        cv.drawCircle(W / 2, 600, rr, P("#D6A650", 90 * (1 - rr / 840), 4))
    compass(cv, W / 2, 600, 270, t * 40 * (1 - k) + 10 * k, 120)
    # calendar page
    cv.save(); cv.translate(W / 2, 600); cv.rotate(math.sin(t * 30) * spin * .2)
    page = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-230, -170, 460, 340), 24, 24)
    cv.drawRRect(page, lin((0, -170), (0, 170), ["#F4E8CC", "#E2CB94"])); cv.drawRRect(page, P("#7A5426", 255, 5))
    cv.drawRect(skia.Rect.MakeXYWH(-230, -170, 460, 70), P("#8E2B24"))
    for x in (-130, 130): cv.drawCircle(x, -170, 16, P("#3A2A18"))
    sz = fit("8888", "title", 190, 400)
    text_c(cv, str(yr), 0, 115, font("title", sz), "#3A2410", 255, False)
    cv.restore()
    tl = seg_bounds[si][0] + end
    if t >= tl:
        cv.drawCircle(W / 2, 600, 300 + 600 * eo((t - tl) / .5), P("#F3D48F", 200 * (1 - clamp((t - tl) / .5)), 10))
    if p.get("place") and lt > end:
        q = clamp((lt - end) / .35)
        cv.save(); cv.translate(W / 2, 900); cv.scale(.8 + .2 * eback(q), .8 + .2 * eback(q))
        gold(cv, p["place"], 0, 0, fit(p["place"], "title", 120, W * .85), 255 * q); cv.restore()
    return dict(mood="surprised" if lt < end else "neutral", look=(0, -1), surprise=.4 * (1 - k))

def sc_versus(cv, p, lt, dur, si, t):
    base, top = 1000, 380
    vl, vr = p["left"], p["right"]; mx = max(vl, vr)
    for side, val, lab, key, c0, c1 in ((-1, vl, p.get("left_label", ""), p.get("left_on"), "#D9806A", "#8E2B24"),
                                         (1, vr, p.get("right_label", ""), p.get("right_on"), "#F3D48F", "#B07A34")):
        tw, _ = _k_on(si, key, t)
        q = eo((t - tw) / 1.1) if tw is not None and t >= tw else (eo((lt - .2 - (side > 0) * .6) / 1.1) if key is None else 0)
        x = W / 2 + side * 220; hgt = (base - top) * (val / mx) * q
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 110, base - (base - top), 220, base - top), 20, 20), P("#0B1224", 160))
        if hgt > 2:
            cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x - 110, base - hgt, 220, hgt), 20, 20), lin((0, base - hgt), (0, base), [c0, c1]))
        a = 255 * clamp(q * 3)
        text_c(cv, _num(int(round(val * q))), x, base - hgt - 30, font("title", fit(_num(val), "title", 96, 300)), c0, a)
        text_c(cv, lab, x, base + 70, font("sub", 50), "#F1E4C4", 255 * clamp(lt / .4))
    gold(cv, "VS", W / 2, 640, 90, 255 * clamp(lt / .3))
    return dict(mood="serious", look=(0, -.6))

def sc_verdict(cv, p, lt, dur, si, t):
    cx, cy = W / 2, 560
    q = eback(lt / .4)
    cv.save(); cv.translate(cx, cy); cv.rotate(-2 + 2 * math.sin(t)); cv.scale(q, q)
    card = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-400, -220, 800, 440), 28, 28)
    cv.drawRRect(card, lin((0, -220), (0, 220), ["#F0DFB4", "#E2CB94"])); cv.drawRRect(card, P("#6E4E22", 255, 6))
    text_c(cv, "ON RACONTE QUE…", 0, -130, font("title", 44), "#7A5426", 255, False)
    claim = p.get("claim", ""); words_ = claim.split(); lines, cur = [], ""
    for w in words_:
        if font("sub", 76).measureText((cur + " " + w).strip()) > 700: lines.append(cur); cur = w
        else: cur = (cur + " " + w).strip()
    lines.append(cur)
    for i, ln in enumerate(lines[:3]):
        text_c(cv, ln, 0, -20 + i * 84, font("sub", 76), "#3A2410", 255, False)
    cv.restore()
    ts, k = _k_on(si, p.get("stamp_on"), t, .2)
    if ts is not None and t >= ts:
        lab = p.get("stamp", "FAUX"); good = lab.upper().startswith("VRAI")
        c = "#3FA45B" if good else "#E0402F"
        cv.save(); cv.translate(cx + 170 + _shake(ts, t, 10), cy + 250); cv.rotate(-14); s_ = 2.3 - 1.3 * eo(k); cv.scale(s_, s_)
        f = font("title", 130); w = f.measureText(lab)
        rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 - 40, -125, w + 80, 165), 20, 20)
        cv.drawRRect(rr, P("#0B1224", 200 * k)); cv.drawRRect(rr, P(c, 255 * k, 14)); cv.drawString(lab, -w / 2, 0, f, P(c, 255 * k)); cv.restore()
        return dict(mood="smug" if not good else "happy", look=(-.5, -.6))
    return dict(mood="curious", look=(-.5, -.6))

def sc_quote(cv, p, lt, dur, si, t):
    cx, top, wd, hg = W / 2, 300, 880, 640
    q = eo(lt / .5)
    cv.save(); cv.translate(cx, top + hg / 2); cv.scale(.9 + .1 * q, .9 + .1 * q); cv.translate(-cx, -(top + hg / 2))
    r = skia.Rect.MakeXYWH(cx - wd / 2, top, wd, hg)
    cv.drawRect(r, lin((0, top), (0, top + hg), ["#F0DFB4", "#E2CB94"]))
    cv.drawRect(r, lin((cx - wd / 2, 0), (cx + wd / 2, 0), [("#8A6A3A", 110), ("#8A6A3A", 0), ("#8A6A3A", 0), ("#8A6A3A", 110)], [0, .12, .88, 1]))
    if p.get("title"): text_c(cv, p["title"], cx, top + 90, font("title", 50), "#7A5426", 255, False)
    # handwriting: the segment's own words appear as they are spoken
    sw = [w for w in words if w["seg"] == si]
    f = font("sub", 74); x0, x, y = cx - wd / 2 + 60, cx - wd / 2 + 60, top + 200; pen = (x0, y)
    sp = f.measureText(" ")
    for w in sw:
        ww = f.measureText(w["text"])
        if x + ww > cx + wd / 2 - 60: x = x0; y += 90
        if y > top + hg - 60: break
        k = clamp((t - w["t0"]) / max(.05, w["t1"] - w["t0"]))
        if k > 0:
            cv.save(); cv.clipRect(skia.Rect.MakeXYWH(x - 4, y - 70, (ww + 8) * k, 100))
            cv.drawString(w["text"], x, y, f, P("#2A1A0C")); cv.restore()
            pen = (x + ww * k, y)
        x += ww + sp
    if p.get("sign") and sw and t > sw[-1]["t1"]:
        text_c(cv, p["sign"], cx + 160, top + hg - 50, font("sub", 52), "#7A5426", 255 * clamp((t - sw[-1]["t1"]) / .4), False)
    cv.restore()
    draw_quill(cv, pen[0] + 6, pen[1] + 4 + 6 * math.sin(t * 25), 28, .55)
    return dict(mood="serious", look=(-.6, -.8))

from character import draw_quill
SCENES.update(counter=sc_counter, year=sc_year, versus=sc_versus, verdict=sc_verdict, quote=sc_quote)

def common_sfx(si, seg, p, a_, b_, ty):
    if ty == "counter":
        ts = word_time(si, p.get("slam_on"))
        end = ts if ts is not None else a_ + min(1.4, (b_ - a_) * .5)
        for k in np.arange(a_ + .05, end, .07): put(sfx, tick(), k, .2)
        put(sfx, boom(), end, .9)
    if ty == "year":
        tl = word_time(si, p.get("land_on")); end = a_ + max(1.0, (tl - a_) if tl is not None else min(1.6, (b_ - a_) * .6))
        put(music, riser(max(.4, end - a_)), a_, .3); put(sfx, thud(), end, .8)
    if ty == "versus":
        for key in ("left_on", "right_on"):
            tw = word_time(si, p.get(key)); tw is not None and put(sfx, whoosh(.6), tw, .3)
    if ty == "verdict":
        ts = word_time(si, p.get("stamp_on")); ts is not None and (put(sfx, thud(), ts + .12, 1.0), put(music, taiko(1.2, 60), ts + .1, .5))
    if ty == "quote":
        for w in words:
            if w["seg"] == si: put(sfx, rng.standard_normal(int(.05 * SR)) * .08, w["t0"], .5)   # pen scratch

SFX_HOOKS.append(common_sfx)
