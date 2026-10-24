# Scene pack: "Le vol de la Joconde" (loaded by engine.py with exec, shares its globals)

# ------------------------------------------------------------------ props
def museum_wall(cv, t, night=0.0, y0=240, y1=1040):
    top, bot = ("#6A2028", "#3E1116") if night < .5 else ("#2A2440", "#15122A")
    cv.drawRect(skia.Rect.MakeXYWH(40, y0, W - 80, y1 - y0), lin((0, y0), (0, y1), [top, bot]))
    # damask pattern
    pat = P("#E2B661", 22 if night < .5 else 12, 2)
    for gy in range(int(y0) + 40, int(y1) - 40, 110):
        for gx in range(90, W - 60, 120):
            ox = 60 if (gy // 110) % 2 else 0
            x = gx + ox
            if x > W - 70: continue
            d = skia.Path(); d.moveTo(x, gy - 26); d.quadTo(x + 22, gy, x, gy + 26); d.quadTo(x - 22, gy, x, gy - 26)
            cv.drawPath(d, pat)
    # mouldings
    cv.drawRect(skia.Rect.MakeXYWH(40, y0, W - 80, 16), lin((0, y0), (0, y0 + 16), ["#E9C47A", "#8A5A22"]))
    cv.drawRect(skia.Rect.MakeXYWH(40, y1 - 70, W - 80, 70), lin((0, y1 - 70), (0, y1), ["#3A2A1C", "#1A120A"]))
    cv.drawRect(skia.Rect.MakeXYWH(40, y1 - 74, W - 80, 6), P("#C9A04E", 200))
    cv.drawRect(skia.Rect.MakeXYWH(40, y0, W - 80, y1 - y0), P("#C9A04E", 120, 4))
    if night > 0:
        cv.drawRect(skia.Rect.MakeXYWH(40, y0, W - 80, y1 - y0), P("#0A1430", 150 * night))

def picture_light(cv, cx, top, w, a=255):
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(cx - w * .3, top - 34, w * .6, 16), 8, 8), P("#C9A04E", a))
    cone = skia.Path(); cone.moveTo(cx - w * .3, top - 20); cone.lineTo(cx + w * .3, top - 20)
    cone.lineTo(cx + w * .75, top + 420); cone.lineTo(cx - w * .75, top + 420); cone.close()
    cv.drawPath(cone, lin((0, top - 20), (0, top + 420), [("#FFE7A8", 70 * a / 255), ("#FFE7A8", 0)]))

def gold_frame(cv, x, y, w, h, a=255, bar=34):
    cv.drawRect(skia.Rect.MakeXYWH(x - bar, y - bar, w + 2 * bar, h + 2 * bar),
                lin((x, y - bar), (x + w, y + h + bar), [("#F7DD9C", a), ("#B07A34", a), ("#E2B661", a), ("#7A4E1C", a)], [0, .35, .65, 1]))
    cv.drawRect(skia.Rect.MakeXYWH(x - bar, y - bar, w + 2 * bar, h + 2 * bar), P("#5A3A14", a, 4))
    cv.drawRect(skia.Rect.MakeXYWH(x - 8, y - 8, w + 16, h + 16), P("#5A3A14", a, 5))
    cv.drawRect(skia.Rect.MakeXYWH(x - bar / 2, y - bar / 2, w + bar, h + bar), P("#FBE7B0", a * .5, 2))
    for cx_, cy_ in ((x - bar / 2, y - bar / 2), (x + w + bar / 2, y - bar / 2), (x - bar / 2, y + h + bar / 2), (x + w + bar / 2, y + h + bar / 2)):
        cv.drawCircle(cx_, cy_, bar * .45, P("#F3D48F", a)); cv.drawCircle(cx_, cy_, bar * .45, P("#7A4E1C", a, 3))

def mona_canvas(cv, x, y, w, h, a=255):
    """Stylised homage to the (public-domain) portrait: sfumato landscape, dark dress, folded hands."""
    cv.save(); cv.clipRect(skia.Rect.MakeXYWH(x, y, w, h), doAntiAlias=True)
    cv.drawRect(skia.Rect.MakeXYWH(x, y, w, h), lin((0, y), (0, y + h), [("#A9B48E", a), ("#7E8A5C", a), ("#4E4126", a)], [0, .45, 1]))
    m = skia.Path(); m.moveTo(x, y + h * .38)
    m.quadTo(x + w * .15, y + h * .26, x + w * .3, y + h * .34); m.lineTo(x + w * .3, y + h * .5); m.lineTo(x, y + h * .5); m.close()
    cv.drawPath(m, P("#7E9A98", a * .7))
    m2 = skia.Path(); m2.moveTo(x + w, y + h * .36)
    m2.quadTo(x + w * .85, y + h * .24, x + w * .7, y + h * .32); m2.lineTo(x + w * .7, y + h * .5); m2.lineTo(x + w, y + h * .5); m2.close()
    cv.drawPath(m2, P("#7E9A98", a * .7))
    road = skia.Path(); road.moveTo(x + w * .08, y + h * .52); road.quadTo(x + w * .2, y + h * .42, x + w * .14, y + h * .36)
    cv.drawPath(road, P("#D9C08A", a * .6, 5))
    cx = x + w / 2
    # hair (behind)
    hair = skia.Path(); hair.addOval(skia.Rect.MakeXYWH(cx - w * .2, y + h * .1, w * .4, h * .5)); cv.drawPath(hair, P("#2A1E12", a))
    # dress / shoulders
    dr = skia.Path(); dr.moveTo(cx - w * .12, y + h * .44)
    dr.cubicTo(cx - w * .32, y + h * .5, cx - w * .44, y + h * .7, cx - w * .48, y + h * 1.02)
    dr.lineTo(cx + w * .48, y + h * 1.02); dr.cubicTo(cx + w * .44, y + h * .7, cx + w * .32, y + h * .5, cx + w * .12, y + h * .44); dr.close()
    cv.drawPath(dr, lin((0, y + h * .44), (0, y + h), [("#3B2E1C", a), ("#221A10", a)]))
    neck = skia.Path(); neck.moveTo(cx - w * .14, y + h * .5); neck.quadTo(cx, y + h * .6, cx + w * .14, y + h * .5); neck.lineTo(cx + w * .1, y + h * .44); neck.lineTo(cx - w * .1, y + h * .44); neck.close()
    cv.drawPath(neck, P("#C99A60", a))
    # face
    cv.drawOval(skia.Rect.MakeXYWH(cx - w * .12, y + h * .2, w * .24, h * .27), lin((0, y + h * .2), (0, y + h * .47), [("#E2BC84", a), ("#B98A52", a)]))
    for s_ in (-1, 1):
        cv.drawOval(skia.Rect.MakeXYWH(cx + s_ * w * .05 - w * .025, y + h * .3, w * .05, h * .015), P("#4A3220", a * .8))
    sm = skia.Path(); sm.moveTo(cx - w * .035, y + h * .405); sm.quadTo(cx, y + h * .418, cx + w * .035, y + h * .402)
    cv.drawPath(sm, P("#7A4A2C", a, 2))
    # hands
    cv.drawOval(skia.Rect.MakeXYWH(cx - w * .22, y + h * .78, w * .26, h * .08), P("#D2A86E", a))
    cv.drawOval(skia.Rect.MakeXYWH(cx - w * .06, y + h * .8, w * .26, h * .08), P("#C99A60", a))
    # varnish glow
    cv.drawRect(skia.Rect.MakeXYWH(x, y, w, h), rad((cx, y + h * .35), h * .7, [("#FFE7A8", 30 * a / 255), ("#000000", 60 * a / 255)]))
    cv.restore()

def mona(cv, cx, cy, w, h, a=255):
    gold_frame(cv, cx - w / 2, cy - h / 2, w, h, a)
    mona_canvas(cv, cx - w / 2, cy - h / 2, w, h, a)

def hooks4(cv, x, y, w, h, a=255):
    for hx, hy in ((x + 18, y + 10), (x + w - 18, y + 10), (x + 18, y + h - 14), (x + w - 18, y + h - 14)):
        cv.drawLine(hx, hy - 16, hx, hy + 6, P("#2A2A2A", a, 7))
        hk = skia.Path(); hk.moveTo(hx, hy + 6); hk.quadTo(hx, hy + 22, hx + 12, hy + 16)
        cv.drawPath(hk, P("#3A3A3A", a, 6))

def person(cv, x, y, s, kind, t, ph=0.0, a=255, flowers=False):
    cv.save(); cv.translate(x, y + 3 * math.sin(t * 1.7 + ph)); cv.scale(s, s); cv.rotate(2.5 * math.sin(t * 1.1 + ph))
    body = skia.Path(); body.moveTo(-46, 0); body.lineTo(-34, -120); body.quadTo(0, -140, 34, -120); body.lineTo(46, 0); body.close()
    c = "#0B0A12"
    cv.drawPath(body, P(c, a))
    cv.drawCircle(0, -158, 30, P(c, a))
    if kind == "bowler":
        cv.drawOval(skia.Rect.MakeXYWH(-40, -186, 80, 16), P(c, a)); cv.drawOval(skia.Rect.MakeXYWH(-26, -214, 52, 44), P(c, a))
    elif kind == "lady":
        cv.drawOval(skia.Rect.MakeXYWH(-62, -192, 124, 24), P(c, a)); cv.drawOval(skia.Rect.MakeXYWH(-30, -214, 60, 36), P(c, a))
        cv.drawCircle(26, -206, 10, P("#8E2B24", a))
    elif kind == "cap":
        cv.drawOval(skia.Rect.MakeXYWH(-34, -196, 68, 30), P(c, a)); cv.drawRect(skia.Rect.MakeXYWH(0, -178, 40, 6), P(c, a))
    if flowers:
        cv.drawLine(30, -80, 44, -140, P("#2F5B3A", a, 4))
        for k, cc in enumerate(("#E25A47", "#F6C85A", "#F1E4C4")):
            cv.drawCircle(44 + 10 * math.cos(k * 2.1), -146 + 10 * math.sin(k * 2.1), 9, P(cc, a))
    cv.drawPath(body, P("#E2B661", a * .25, 2))
    cv.restore()

def worker(cv, x, y, s, t, a=255, carry=False, glass=False):
    """Faceless silhouette in a white work smock."""
    cv.save(); cv.translate(x, y); cv.scale(s, s)
    for side in (-1, 1):
        cv.drawLine(side * 16, -10, side * 18 + 10 * math.sin(t * 7 + side), 0, P("#1A1A22", a, 16))
    sm = skia.Path(); sm.moveTo(-48, -20); sm.lineTo(-38, -150); sm.quadTo(0, -168, 38, -150); sm.lineTo(48, -20); sm.close()
    cv.drawPath(sm, lin((0, -168), (0, -20), [("#F3EEE2", a), ("#BDB6A6", a)])); cv.drawPath(sm, P("#3A3A3A", a, 3))
    cv.drawCircle(0, -190, 30, P("#1A1A22", a))
    cv.drawOval(skia.Rect.MakeXYWH(-34, -226, 68, 28), P("#1A1A22", a)); cv.drawRect(skia.Rect.MakeXYWH(0, -208, 38, 6), P("#1A1A22", a))
    if carry:    # rectangular bulge under the smock
        cv.drawRect(skia.Rect.MakeXYWH(-30, -130, 60, 80), P("#D9D2C2", a)); cv.drawRect(skia.Rect.MakeXYWH(-30, -130, 60, 80), P("#8A8270", a, 2))
    if glass:
        cv.save(); cv.rotate(-12)
        cv.drawRect(skia.Rect.MakeXYWH(40, -170, 70, 110), P("#BFE3F5", a * .35)); cv.drawRect(skia.Rect.MakeXYWH(40, -170, 70, 110), P("#E6F6FF", a * .9, 3))
        cv.drawLine(52, -160, 70, -140, P("#FFFFFF", a * .8, 3))
        cv.restore()
    cv.restore()

def stamp(cv, x, y, label, k, color="#E0402F", rot=-12, size=84):
    if k <= 0: return
    sc = 2.2 - 1.2 * eo(k)
    cv.save(); cv.translate(x, y); cv.rotate(rot); cv.scale(sc, sc)
    f = font("title", size); w = f.measureText(label); a = 255 * clamp(k * 3)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 - 36, -size - 10, w + 72, size + 44), 14, 14)
    cv.drawRRect(rr, P("#14060A", 140 * a / 255)); cv.drawRRect(rr, P(color, a, 9))
    cv.drawString(label, -w / 2, 0, f, P(color, a)); cv.restore()

def date_pill(cv, x, y, label, k):
    if k <= 0: return
    cv.save(); cv.translate(x, y); s = eback(k); cv.scale(s, s)
    f = font("title", 40); w = f.measureText(label)
    rr = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-w / 2 - 30, -44, w + 60, 62), 31, 31)
    cv.drawRRect(rr, P("#0B1224", 225)); cv.drawRRect(rr, P("#D6A650", 255, 3))
    cv.drawString(label, -w / 2, 0, f, P("#F0CF85")); cv.restore()

def newspaper(cv, cx, cy, k, t, head, sub):
    if k <= 0: return
    cv.save(); cv.translate(cx, cy); cv.rotate(-720 * (1 - eo(k)) - 6); s = .2 + .8 * eo(k); cv.scale(s, s)
    w, h = 640, 460
    cv.drawRect(skia.Rect.MakeXYWH(-w / 2 + 10, -h / 2 + 14, w, h), P("#000000", 120))
    cv.drawRect(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), lin((0, -h / 2), (0, h / 2), ["#EFE6D0", "#D9CBA8"]))
    text_c(cv, "ÉDITION SPÉCIALE", 0, -h / 2 + 62, font("title", 44), "#2A1E12", shadow=False)
    cv.drawLine(-w / 2 + 30, -h / 2 + 84, w / 2 - 30, -h / 2 + 84, P("#2A1E12", 255, 4))
    cv.drawLine(-w / 2 + 30, -h / 2 + 94, w / 2 - 30, -h / 2 + 94, P("#2A1E12", 255, 2))
    hf = font("title", fit(head, "title", 64, w - 60))
    text_c(cv, head, 0, -h / 2 + 175, hf, "#8E1A14", shadow=False)
    text_c(cv, sub, 0, -h / 2 + 230, font("sub", 40), "#2A1E12", shadow=False)
    for i in range(6):   # fake columns
        for j in (-1, 1):
            cv.drawLine(j * 150 - 120, -h / 2 + 280 + i * 26, j * 150 + 120, -h / 2 + 280 + i * 26, P("#6E5E44", 180, 5))
    cv.restore()

def suspect_card(cv, cx, cy, name, role, t, a=255):
    w, h = 380, 520
    cv.save(); cv.translate(cx, cy)
    cv.drawRect(skia.Rect.MakeXYWH(-w / 2 + 8, -h / 2 + 12, w, h), P("#000000", 110 * a / 255))
    cv.drawRect(skia.Rect.MakeXYWH(-w / 2, -h / 2, w, h), lin((0, -h / 2), (0, h / 2), [("#EAD7AA", a), ("#CDB27A", a)]))
    cv.drawRect(skia.Rect.MakeXYWH(-w / 2 + 14, -h / 2 + 14, w - 28, h - 28), P("#6E4E22", a, 3))
    text_c(cv, "SUSPECT", 0, -h / 2 + 74, font("title", 50), "#6E1A14", a, shadow=False)
    cv.drawRect(skia.Rect.MakeXYWH(-120, -h / 2 + 100, 240, 230), P("#2A2016", a))
    cv.drawCircle(0, -h / 2 + 190, 52, P("#0E0B08", a))
    b = skia.Path(); b.moveTo(-95, -h / 2 + 330); b.quadTo(0, -h / 2 + 225, 95, -h / 2 + 330); b.close(); cv.drawPath(b, P("#0E0B08", a))
    text_c(cv, "?", 0, -h / 2 + 215, font("title", 70), "#E2B661", a * .9, shadow=False)
    text_c(cv, name, 0, h / 2 - 110, font("title", fit(name, "title", 48, w - 50)), "#2A1E12", a, shadow=False)
    text_c(cv, role, 0, h / 2 - 58, font("sub", 40), "#4A3420", a, shadow=False)
    cv.restore()

def bars(cv, cx, cy, k):
    if k <= 0: return
    w, h = 380, 520; drop = (1 - ebounce(k)) * -h
    cv.save(); cv.clipRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2, w, h))
    for i in range(6):
        x = cx - w / 2 + 30 + i * (w - 60) / 5
        cv.drawRect(skia.Rect.MakeXYWH(x - 9, cy - h / 2 + drop, 18, h), lin((x - 9, 0), (x + 9, 0), ["#9AA3B5", "#4A5166"]))
    cv.drawRect(skia.Rect.MakeXYWH(cx - w / 2, cy - h / 2 + 40 + drop, w, 18), P("#5A6070"))
    cv.restore()

# ------------------------------------------------------------------ scenes
def sc_wall(cv, p, lt, dur, si, t):
    museum_wall(cv, t)
    px, py, pw, ph = W / 2, 600, 280, 350
    picture_light(cv, px, py - ph / 2 - 30, pw)
    cv.drawRect(skia.Rect.MakeXYWH(px - pw / 2 - 30, py - ph / 2 - 30, pw + 60, ph + 60), P("#8A3A40", 110))
    cv.drawRect(skia.Rect.MakeXYWH(px - pw / 2 - 30, py - ph / 2 - 30, pw + 60, ph + 60), P("#C9A04E", 60, 2))
    hooks4(cv, px - pw / 2 - 30, py - ph / 2 - 30, pw + 60, ph + 60)
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(px - 90, py + ph / 2 + 50, 180, 40), 6, 6), lin((0, 0), (0, 40), ["#F3D48F", "#B07A34"]))
    text_c(cv, "LA JOCONDE", px, py + ph / 2 + 79, font("title", 24), "#3A2410", shadow=False)
    crowd = [(150, "bowler", 0, False), (300, "lady", 1.3, True), (430, "cap", 2.1, False), (650, "lady", .7, False),
             (780, "bowler", 2.8, True), (930, "cap", 1.9, False), (230, "lady", 3.3, False), (860, "bowler", 4.1, False)]
    for i, (x, kind, ph_, fl) in enumerate(crowd):
        k = eo((lt - .1 - .08 * i) / .5)
        if k <= 0: continue
        y = 1040 + (1 - k) * 200 - (30 if i >= 6 else 0)
        person(cv, x, y, .95 if i < 6 else .8, kind, t, ph_, a=255 * k, flowers=fl)
    ts = word_time(si, p.get("slam_on", "vide"))
    punch = 1 + (.18 * math.exp(-(t - ts) * 8) if ts is not None and t >= ts else 0)
    if ts is not None and t >= ts - .1:
        k = eback((t - ts + .1) / .3)
        cv.save(); cv.translate(W / 2, 330); cv.scale(k * punch, k * punch)
        gold(cv, "UN MUR VIDE", 0, 0, 100); cv.restore()
    fl = math.exp(-(t - ts) * 8) if ts is not None and t >= ts else 0
    if fl > .01: cv.drawRect(skia.Rect.MakeWH(W, H), P("#FFE2A8", 70 * fl))
    return dict(mood="surprised" if lt < 1.2 else "neutral", surprise=fl * .8, look=(.6 if lt > .5 else 0, -.6))

def sc_night(cv, p, lt, dur, si, t):
    museum_wall(cv, t, night=1.0)
    # moonlight from a window
    for k in range(3):
        sh = skia.Path(); x0 = 120 + k * 70
        sh.moveTo(x0, 240); sh.lineTo(x0 + 50, 240); sh.lineTo(x0 + 330, 1000); sh.lineTo(x0 + 250, 1000); sh.close()
        cv.drawPath(sh, lin((0, 240), (0, 1000), [("#BFD7FF", 40), ("#BFD7FF", 0)]))
    px, py, pw, ph = W / 2 + 60, 660, 240, 330
    gold_frame(cv, px - pw / 2, py - ph / 2, pw, ph, 230)
    tk = word_time(si, p.get("take_on", "décroche")); tb = word_time(si, p.get("smock_on", "blouse"))
    lift = eo((t - tk) / 1.2) if tk is not None and t >= tk else 0
    if lift < 1:
        cv.save(); cv.translate(140 * lift, 260 * lift); cv.scale(1 - .55 * lift, 1 - .55 * lift)
        mona_canvas(cv, px - pw / 2 + 120 * lift, py - ph / 2 + 300 * lift * 0, pw, ph, 255 * (1 - lift * .2))
        cv.restore()
    if lift > .02:
        cv.drawRect(skia.Rect.MakeXYWH(px - pw / 2, py - ph / 2, pw, ph), P("#0E0B14", 255 * min(1, lift * 2)))
    # closet door with glowing eyes
    dx = 140
    cv.drawRect(skia.Rect.MakeXYWH(dx - 60, 640, 150, 330), P("#1A1424")); cv.drawRect(skia.Rect.MakeXYWH(dx - 60, 640, 150, 330), P("#C9A04E", 120, 3))
    open_ = eo(lt / .8) * .5
    cv.drawRect(skia.Rect.MakeXYWH(dx - 60, 640, 150 * open_, 330), P("#050308"))
    if open_ > .2 and (int(t * 3) % 5):
        for ex in (dx - 30, dx - 8): cv.drawOval(skia.Rect.MakeXYWH(ex, 760, 14, 8), P("#F6C85A"))
    # thief walks off with the canvas under the smock
    if tb is not None and t >= tb - .4:
        q = (t - tb + .4) / 1.6
        worker(cv, 700 + 420 * eo(q), 1000, .85, t, carry=True)
    date_pill(cv, W / 2, 315, p.get("date", "21 AOÛT 1911"), eo(lt / .4))
    k2 = eo((lt - .6) / .4)
    if k2 > 0: text_c(cv, p.get("pill", "MUSÉE FERMÉ"), W / 2, 385, font("sub", 46), "#F1E4C4", 255 * k2)
    return dict(mood="worried", look=(.7, -.6))

def sc_discover(cv, p, lt, dur, si, t):
    museum_wall(cv, t)
    px, py, pw, ph = W / 2 + 140, 640, 240, 320
    cv.drawRect(skia.Rect.MakeXYWH(px - pw / 2 - 30, py - ph / 2 - 30, pw + 60, ph + 60), P("#8A3A40", 110))
    hooks4(cv, px - pw / 2 - 30, py - ph / 2 - 30, pw + 60, ph + 60)
    # painter with easel
    ex = 250
    cv.drawLine(ex - 70, 980, ex, 620, P("#6E4E22", 255, 10)); cv.drawLine(ex + 70, 980, ex, 620, P("#6E4E22", 255, 10))
    cv.drawRect(skia.Rect.MakeXYWH(ex - 90, 640, 180, 220), P("#F4E8CC")); cv.drawRect(skia.Rect.MakeXYWH(ex - 90, 640, 180, 220), P("#6E4E22", 255, 5))
    person(cv, ex + 150, 1010, .9, "cap", t, .5)
    q = word_time(si, "place") or (seg_bounds[si][0] + 1.2)
    if t >= q:
        k = eback((t - q) / .35)
        cv.save(); cv.translate(ex + 150, 760 - 20 * math.sin(t * 4)); cv.scale(k, k)
        text_c(cv, "?", 0, 0, font("title", 120), "#F6C85A"); cv.restore()
    date_pill(cv, W / 2, 315, p.get("date", "22 AOÛT 1911"), eo(lt / .4))
    tp = word_time(si, p.get("panic_on", "panique"))
    alarm = 0
    if tp is not None and t >= tp - .15:
        k = (t - tp + .15) / .6
        alarm = .5 + .5 * math.sin(t * 18)
        cv.drawRect(skia.Rect.MakeWH(W, H), P("#C0392B", 45 * alarm))
        newspaper(cv, W / 2, 640, k, t, "LA JOCONDE A DISPARU !", "Vol au musée du Louvre")
    return dict(mood="surprised" if tp is not None and t >= tp else "neutral", surprise=.7 if (tp is not None and t >= tp) else 0, look=(.6, -.6))

def sc_suspects(cv, p, lt, dur, si, t):
    k1, k2 = eback(lt / .45), eback((lt - .15) / .45)
    cv.save(); cv.translate(290, 600); cv.rotate(-4); cv.scale(k1, k1); cv.translate(-290, -600)
    suspect_card(cv, 290, 600, "APOLLINAIRE", "poète", t); cv.restore()
    cv.save(); cv.translate(790, 610); cv.rotate(4); cv.scale(k2, k2); cv.translate(-790, -610)
    suspect_card(cv, 790, 610, "PICASSO", "peintre", t); cv.restore()
    ta = word_time(si, p.get("arrest_on", "arrêté")); tq = word_time(si, p.get("ask_on", "interrogé")); ti = word_time(si, p.get("free_on", "eux"))
    if ta is not None and t >= ta: bars(cv, 290, 600, (t - ta) / .7)
    if tq is not None and t >= tq:
        k = eback((t - tq) / .35); cv.save(); cv.translate(790, 660); cv.scale(k, k)
        text_c(cv, "?", 0, 0, font("title", 200), "#F6C85A"); cv.restore()
    if ti is not None and t >= ti:
        stamp(cv, W / 2, 640, "INNOCENTS", (t - ti) / .25, color="#3FAE6A", rot=-8, size=96)
    return dict(mood="serious", look=(0, -1))

def sc_thief(cv, p, lt, dur, si, t):
    cone = skia.Path(); cone.moveTo(W / 2 - 40, 220); cone.lineTo(W / 2 + 40, 220); cone.lineTo(W / 2 + 300, 1000); cone.lineTo(W / 2 - 300, 1000); cone.close()
    cv.drawPath(cone, lin((0, 220), (0, 1000), [("#FFF2C8", 90), ("#FFF2C8", 10)]))
    cv.drawOval(skia.Rect.MakeXYWH(W / 2 - 300, 960, 600, 80), P("#FFF2C8", 50))
    k = eo(lt / .6)
    worker(cv, W / 2 - 40, 1000, 1.25 * (.9 + .1 * k), t, a=255 * k, glass=True)
    name = p.get("name", "VINCENZO PERUGGIA")
    tn = word_time(si, p.get("name_on", "vincenzo")) or (seg_bounds[si][0] + .5)
    n_ = int(len(name) * clamp((t - tn) / 1.0))
    if n_:
        sz = fit(name, "title", 92, W * .86); fw = font("title", sz).measureText(name); part = name[:n_]
        gold(cv, part, W / 2 - fw / 2 + font("title", sz).measureText(part) / 2, 330, sz)
    if t > tn + .9: text_c(cv, p.get("sub", "vitrier italien"), W / 2, 395, font("sub", 52), "#F1E4C4", 255 * clamp((t - tn - .9) / .3))
    tw = word_time(si, p.get("pill_on", "travaillé"))
    if tw is not None and t >= tw: date_pill(cv, W / 2, 470, p.get("pill", "ANCIEN EMPLOYÉ DU LOUVRE"), eo((t - tw) / .35))
    return dict(mood="serious", look=(-.6, -.6))

def sc_hideout(cv, p, lt, dur, si, t):
    cv.drawRect(skia.Rect.MakeXYWH(40, 240, W - 80, 800), lin((0, 240), (0, 1040), ["#2E2436", "#17121E"]))
    roof = skia.Path(); roof.moveTo(40, 240); roof.lineTo(W - 40, 240); roof.lineTo(W - 40, 420); roof.lineTo(40, 640); roof.close()
    cv.drawPath(roof, P("#1E1826"))
    for k in range(6): cv.drawLine(40 + k * 180, 240, 40 + k * 180, 640 - k * 40, P("#3A2E46", 255, 6))
    cv.drawRect(skia.Rect.MakeXYWH(40, 240, W - 80, 800), P("#C9A04E", 90, 3))
    # small window with moon
    cv.drawRect(skia.Rect.MakeXYWH(700, 470, 180, 150), P("#0E1A36")); cv.drawCircle(820, 520, 30, P("#F3E6C0"))
    cv.drawRect(skia.Rect.MakeXYWH(700, 470, 180, 150), P("#6E4E22", 255, 8)); cv.drawLine(790, 470, 790, 620, P("#6E4E22", 255, 6))
    # bed
    cv.drawRect(skia.Rect.MakeXYWH(140, 760, 620, 70), lin((0, 760), (0, 830), ["#D9CBA8", "#A99878"]))
    cv.drawRect(skia.Rect.MakeXYWH(150, 730, 150, 40), P("#EFE6D0"))
    for x in (150, 740): cv.drawRect(skia.Rect.MakeXYWH(x, 700, 20, 300), P("#5A3A1C"))
    cv.drawRect(skia.Rect.MakeXYWH(150, 830, 610, 16), P("#5A3A1C"))
    # suitcase under the bed, glowing
    ls = word_time(si, p.get("case_on", "valise")) or (seg_bounds[si][0] + 1.0)
    glow = clamp((t - ls) / .6)
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(300, 880, 300, 110), 14, 14), lin((0, 880), (0, 990), ["#7A4E2C", "#4A2E18"]))
    cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(300, 880, 300, 110), 14, 14), P("#2A1A0C", 255, 5))
    cv.drawRect(skia.Rect.MakeXYWH(430, 866, 40, 16), P("#C9A04E"))
    if glow > 0:
        cv.drawCircle(450, 935, 260, rad((450, 935), 260, [("#FFD27A", 150 * glow * (.8 + .2 * math.sin(t * 5))), ("#FFD27A", 0)]))
        lid = skia.Path(); lid.moveTo(300, 880); lid.lineTo(600, 880); lid.lineTo(590, 880 - 40 * glow); lid.lineTo(310, 880 - 40 * glow); lid.close()
        cv.drawPath(lid, P("#FFE7A8", 200 * glow))
    # calendar flipping 1911 -> 1913
    cx_, cy_ = 300, 420
    cv.drawRect(skia.Rect.MakeXYWH(cx_ - 90, cy_ - 80, 180, 170), P("#EFE6D0")); cv.drawRect(skia.Rect.MakeXYWH(cx_ - 90, cy_ - 80, 180, 40), P("#B23A2E"))
    years = ["1911", "1912", "1913"]; yi = min(2, int(clamp((lt - .3) / (dur * .7)) * 3))
    flip = ((lt - .3) / (dur * .7) * 3) % 1
    text_c(cv, years[yi], cx_, cy_ + 60, font("title", 62), "#2A1E12", shadow=False)
    if yi < 2 and .7 < flip:
        pg = skia.Path(); q = (flip - .7) / .3
        pg.moveTo(cx_ - 90, cy_ - 40); pg.lineTo(cx_ + 90, cy_ - 40); pg.lineTo(cx_ + 90, cy_ - 40 + 130 * (1 - q)); pg.lineTo(cx_ - 90, cy_ - 40 + 130 * (1 - q)); pg.close()
        cv.drawPath(pg, P("#F7F1E2"))
    td = word_time(si, p.get("big_on", "deux"))
    if td is not None and t >= td:
        k = eback((t - td) / .35); cv.save(); cv.translate(W / 2 + 110, 340); cv.scale(k, k)
        gold(cv, p.get("big", "PLUS DE 2 ANS"), 0, 0, 88); cv.restore()
    return dict(mood="worried", look=(-.6, .3))

def sc_florence(cv, p, lt, dur, si, t):
    tr = word_time(si, p.get("reveal_on", "reconnaît")); tar = word_time(si, p.get("arrest_on", "arrêté#2") ) or word_time(si, "arrêté")
    if tr is None or t < tr:
        # map with route Paris -> Florence
        cv.drawRect(skia.Rect.MakeXYWH(90, 260, W - 180, 720), lin((0, 260), (0, 980), ["#EAD7AA", "#CDB27A"]))
        cv.drawRect(skia.Rect.MakeXYWH(110, 280, W - 220, 680), P("#6E4E22", 255, 3))
        coast = skia.Path(); coast.moveTo(110, 760); coast.cubicTo(300, 700, 420, 860, 560, 800); coast.cubicTo(700, 740, 820, 900, W - 110, 820)
        coast.lineTo(W - 110, 960); coast.lineTo(110, 960); coast.close(); cv.drawPath(coast, P("#9DB6C2", 160))
        alps = skia.Path(); alps.moveTo(470, 600)
        for i in range(8): alps.lineTo(500 + i * 40, 560 if i % 2 == 0 else 610)
        cv.drawPath(alps, P("#8A6E48", 220, 5))
        A, B = (300, 420), (760, 690)
        prog = eo((lt - .2) / 2.0)
        n = 24
        for i in range(int(n * prog)):
            q = i / n; x = A[0] + (B[0] - A[0]) * q; y = A[1] + (B[1] - A[1]) * q - 120 * math.sin(math.pi * q)
            cv.drawCircle(x, y, 6, P("#B23A2E"))
        q = prog; tx = A[0] + (B[0] - A[0]) * q; ty = A[1] + (B[1] - A[1]) * q - 120 * math.sin(math.pi * q)
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(tx - 30, ty - 20, 60, 34), 8, 8), P("#2A1E12")); cv.drawCircle(tx + 20, ty - 26, 8 + 4 * math.sin(t * 9), P("#9AA3B5", 160))
        pin(cv, A[0], A[1], .45); text_c(cv, "PARIS", A[0], A[1] + 50, font("title", 40), "#2A1E12", shadow=False)
        if prog > .9:
            pin(cv, B[0], B[1] - 60 * (1 - ebounce((lt - 2.0) / .6)), .55)
            text_c(cv, "FLORENCE", B[0], B[1] + 56, font("title", 46), "#8E1A14", shadow=False)
        date_pill(cv, W / 2, 330, p.get("date", "FIN 1913"), eo(lt / .4))
        return dict(mood="neutral", look=(.6, -.6))
    # reveal: the painting under a magnifier, then arrest
    lt2 = t - tr
    rays(cv, W / 2, 630, t, 26)
    mona(cv, W / 2, 630, 250 * eback(lt2 / .4), 330 * eback(lt2 / .4))
    mx = W / 2 + 160 * math.cos(lt2 * 2.2); my = 630 + 110 * math.sin(lt2 * 3.1)
    cv.drawLine(mx + 60, my + 60, mx + 150, my + 150, P("#6A4416", 255, 22))
    cv.drawCircle(mx, my, 90, P("#BFE3F5", 70)); cv.drawCircle(mx, my, 90, P("#D6A650", 255, 14)); cv.drawCircle(mx - 28, my - 30, 16, P("#FFFFFF", 150))
    for j in range(8):
        an = j * 45 + lt2 * 90; r = 230 + 20 * math.sin(t * 6 + j)
        x, y = W / 2 + r * math.cos(math.radians(an)), 630 + r * math.sin(math.radians(an))
        cv.drawCircle(x, y, 6 + 3 * math.sin(t * 8 + j), P("#FBE7B0", 200))
    text_c(cv, "C'EST ELLE !", W / 2, 330, font("title", 80), "#F4D692", 255 * clamp(lt2 / .3))
    if tar is not None and t >= tar: stamp(cv, W / 2, 900, "ARRÊTÉ", (t - tar) / .25, size=90)
    return dict(mood="surprised" if lt2 < 1 else "happy", surprise=clamp(1 - lt2) * .7, look=(0, -1))

def sc_fame(cv, p, lt, dur, si, t):
    museum_wall(cv, t)
    rays(cv, W / 2, 640, t, 30)
    mona(cv, W / 2, 640, 250, 330)
    random.seed(int(t * 6))
    for j in range(5):   # camera flashes
        if random.random() < .5:
            x, y = random.uniform(120, W - 120), random.uniform(820, 1000)
            cv.drawCircle(x, y, 60, rad((x, y), 60, [("#FFFFFF", 230), ("#FFFFFF", 0)]))
    txt = p.get("big", "ENCORE PLUS CÉLÈBRE"); n_ = int(len(txt) * clamp((lt - .2) / 1.0))
    if n_:
        sz = fit(txt, "title", 86, W * .86); fw = font("title", sz).measureText(txt); part = txt[:n_]
        gold(cv, part, W / 2 - fw / 2 + font("title", sz).measureText(part) / 2, 330, sz)
    return dict(mood="happy", look=(0, -1))

SCENES.update(wall=sc_wall, night=sc_night, discover=sc_discover, suspects=sc_suspects, thief=sc_thief,
              hideout=sc_hideout, florence=sc_florence, fame=sc_fame)

# ------------------------------------------------------------------ sounds
def murmur(d):
    k = np.arange(int(d * SR)) / SR
    nz = signal.sosfilt(signal.butter(2, [250, 1400], "band", fs=SR, output="sos"), rng.standard_normal(len(k)))
    mod = .6 + .4 * np.sin(2 * np.pi * 1.7 * k) * np.sin(2 * np.pi * .43 * k + 1)
    return nz * mod * np.minimum(1, k / .5) * np.clip((d - k) / .5, 0, 1)

def clank():
    k = np.arange(int(1.2 * SR)) / SR
    s = sum(np.sin(2 * np.pi * f * k) * np.exp(-k * dk) for f, dk in ((523, 4), (1187, 6), (1873, 8), (2650, 10)))
    return .35 * s + .5 * rng.standard_normal(len(k)) * np.exp(-k * 60)

def creak():
    k = np.arange(int(.9 * SR)) / SR
    f = 180 + 120 * np.sin(2 * np.pi * 1.3 * k)
    return np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * .25 * np.sin(np.pi * k / .9) * (np.sin(2 * np.pi * 23 * k) > 0)

def flip():
    k = np.arange(int(.12 * SR)) / SR
    return signal.sosfilt(signal.butter(2, [1500, 6000], "band", fs=SR, output="sos"), rng.standard_normal(len(k))) * np.exp(-k * 30)

def sting():
    k = np.arange(int(1.6 * SR)) / SR
    s = sum(np.sin(2 * np.pi * NOTE(m) * k) for m in (57, 60, 63, 66))
    return s * np.exp(-k * 2.2) * .5

def jc_sfx(si, seg, p, a_, b_, ty):
    if ty == "wall":
        put(sfx, murmur(b_ - a_), a_, .35)
        ts = word_time(si, p.get("slam_on", "vide")); ts is not None and put(sfx, boom(), ts, .8)
    if ty == "night":
        for k in np.arange(0, b_ - a_, .5): put(sfx, tick(), a_ + k, .25)
        put(sfx, creak(), a_ + .2, .35)
        tk = word_time(si, p.get("take_on", "décroche")); tk is not None and put(sfx, whoosh(.8), tk, .4)
        tb = word_time(si, p.get("smock_on", "blouse"))
        if tb is not None:
            for k in range(5): put(sfx, thud(), tb - .3 + k * .32, .18)
    if ty == "discover":
        tp = word_time(si, p.get("panic_on", "panique"))
        if tp is not None:
            put(music, sting(), tp - .1, .5); put(sfx, whoosh(.6), tp - .15, .4); put(sfx, thud(), tp + .45, .7)
            for k in range(6): put(sfx, bell(1600, .25), tp + k * .18, .12)
    if ty == "suspects":
        ta = word_time(si, p.get("arrest_on", "arrêté")); ta is not None and put(sfx, clank(), ta + .3, .6)
        tq = word_time(si, p.get("ask_on", "interrogé")); tq is not None and put(sfx, pop(), tq, .45)
        ti = word_time(si, p.get("free_on", "eux")); ti is not None and put(sfx, thud(), ti + .12, .8)
    if ty == "thief":
        tn = word_time(si, p.get("name_on", "vincenzo")) or (a_ + .5)
        put(music, taiko(1.3, 58), tn, .5)
        for k in range(17): put(sfx, tick(), tn + k * (1.0 / 17), .35)
        tw = word_time(si, p.get("pill_on", "travaillé")); tw is not None and put(sfx, pop(), tw, .35)
    if ty == "hideout":
        for k in np.arange(0, b_ - a_, .55): put(sfx, tick(), a_ + k, .22)
        for k in range(2): put(sfx, flip(), a_ + .3 + (k + .85) * (b_ - a_) * .7 / 3, .5)
        td = word_time(si, p.get("big_on", "deux")); td is not None and put(sfx, thud(), td, .5)
    if ty == "florence":
        for k in np.arange(.2, 2.2, .25): put(sfx, thud(), a_ + k, .12)
        tr = word_time(si, p.get("reveal_on", "reconnaît")); tr is not None and (put(music, bell(NOTE(88)), tr, .3), put(music, bell(NOTE(93)), tr + .15, .25))
        tar = word_time(si, "arrêté"); tar is not None and put(sfx, thud(), tar + .12, .8)
    if ty == "fame":
        for k in np.arange(.1, b_ - a_, .33): put(sfx, pop(), a_ + k, .15)
        motif(a_ + .05, .14)

SFX_HOOKS.append(jc_sfx)
