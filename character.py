"""Archi, the owl archivist of "Encre & Énigmes" — original character.

draw_owl(cv, t, e, costume, look, surprise, blink, point)
  Draws in a unit space where (0, 0) is between the feet and the owl is about
  680 units tall (more with a hat). The caller translates/scales the canvas.
  e        : mouth/beak opening 0..1 (lip-sync)
  costume  : dict(hat=..., coat=..., accessory=...)
  look     : (dx, dy) pupil direction
  surprise : 0..1 (eyes widen, brows up, feathers ruffle)
  blink    : 0..1 eyelid closure
  point    : 0..1 right wing raised / pointing
"""
import math
import skia

def col(h, a=255):
    h = h.lstrip("#")
    return skia.ColorSetARGB(int(max(0, min(255, a))), int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def P(c, a=255, stroke=0):
    p = skia.Paint(AntiAlias=True, Color=col(c, a))
    if stroke:
        p.setStyle(skia.Paint.kStroke_Style); p.setStrokeWidth(stroke)
        p.setStrokeCap(skia.Paint.kRound_Cap); p.setStrokeJoin(skia.Paint.kRound_Join)
    return p

def grad_paint(p0, p1, colors, positions=None):
    p = skia.Paint(AntiAlias=True)
    p.setShader(skia.GradientShader.MakeLinear(points=[p0, p1], colors=[col(c) for c in colors],
                                                positions=positions))
    return p

# ----------------------------------------------------------------- palettes
FEATHER_TOP, FEATHER_MID, FEATHER_BOT = "#B9824A", "#8E5A2E", "#5E3A1C"
FACE = "#F2DDB2"
BELLY = "#E9CF9C"
OUTLINE = "#3B230F"

COATS = {
    "navy":    ("#1F3A6B", "#132648", "#E2B661"),   # body, shadow, trim
    "brown":   ("#7A5230", "#563820", "#D9B36A"),
    "green":   ("#2F5B3A", "#1E3D27", "#D9B36A"),
    "red":     ("#8E2B24", "#5E1A15", "#E2B661"),
    "white":   ("#E9E4D8", "#BDB6A6", "#8A7A5A"),
    "black":   ("#1A1A22", "#0E0E14", "#C9A04E"),
}

def owl_body_path():
    p = skia.Path()
    p.moveTo(0, -14)
    p.cubicTo(-150, -14, -250, -80, -255, -250)
    p.cubicTo(-258, -380, -230, -470, -195, -540)
    p.lineTo(-200, -650)                      # left ear tuft tip
    p.cubicTo(-150, -625, -120, -605, -95, -590)
    p.cubicTo(-40, -612, 40, -612, 95, -590)
    p.cubicTo(120, -605, 150, -625, 200, -650)  # right ear tuft tip
    p.lineTo(195, -540)
    p.cubicTo(230, -470, 258, -380, 255, -250)
    p.cubicTo(250, -80, 150, -14, 0, -14)
    p.close()
    return p

def wing_path(side):
    # feathered wing, pivot at shoulder (0,0), extends down/outwards
    s = side
    p = skia.Path()
    p.moveTo(0, 0)
    p.cubicTo(s * 70, 20, s * 95, 120, s * 80, 230)
    p.lineTo(s * 60, 210); p.lineTo(s * 52, 250); p.lineTo(s * 30, 218); p.lineTo(s * 16, 246)
    p.cubicTo(s * -10, 150, s * -15, 60, 0, 0)
    p.close()
    return p

def draw_quill(cv, x, y, ang, sc=1.0):
    cv.save(); cv.translate(x, y); cv.rotate(ang); cv.scale(sc, sc)
    f = skia.Path(); f.moveTo(0, 0)
    f.cubicTo(-40, -70, -32, -175, 8, -240); f.cubicTo(42, -175, 38, -70, 0, 0); f.close()
    cv.drawPath(f, grad_paint((0, -240), (0, 0), ["#FFFFFF", "#EDE2C6"]))
    cv.drawPath(f, P("#B99A64", 255, 4))
    for k in range(1, 8):
        yy = -29 * k
        cv.drawLine(4, yy + 6, -22 + k * 1.5, yy - 14, P("#CBB488", 255, 3))
        cv.drawLine(4, yy + 6, 26 - k * 1.5, yy - 14, P("#CBB488", 255, 3))
    cv.drawLine(0, 0, 6, -238, P("#9C7B47", 255, 4))
    cv.drawLine(0, 2, -3, 40, P("#1A120A", 255, 9))
    cv.drawCircle(-3, 46, 6, P("#14203F"))       # ink drop on the nib
    cv.restore()

def draw_accessory(cv, kind, t):
    """Drawn at the right wing tip, wing-tip frame (0,0)."""
    if kind == "spyglass":
        cv.save(); cv.rotate(-35)
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-14, -150, 28, 150), 8, 8),
                     grad_paint((-14, 0), (14, 0), ["#F7DD9C", "#C48D3C", "#7A4E1C"]))
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-20, -190, 40, 60), 10, 10),
                     grad_paint((-20, 0), (20, 0), ["#F7DD9C", "#B07A34", "#6A4416"]))
        cv.drawOval(skia.Rect.MakeXYWH(-17, -198, 34, 14), P("#9FD3F0"))
        for yy in (-40, -100):
            cv.drawRect(skia.Rect.MakeXYWH(-16, yy, 32, 8), P("#6A4416"))
        cv.restore()
    elif kind == "magnifier":
        cv.save(); cv.rotate(-20)
        cv.drawLine(0, 0, 0, -90, P("#6A4416", 255, 16))
        cv.drawCircle(0, -140, 52, P("#BFE3F5", 120)); cv.drawCircle(0, -140, 52, P("#D6A650", 255, 12))
        cv.drawCircle(-16, -158, 12, P("#FFFFFF", 160))
        cv.restore()
    elif kind == "lantern":
        cv.save()
        cv.drawLine(0, 0, 0, 40, P("#3A2A18", 255, 5))
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-34, 40, 68, 90), 10, 10), P("#3A2A18"))
        glow = skia.Paint(); glow.setShader(skia.GradientShader.MakeRadial(center=(0, 85), radius=120,
                colors=[col("#FFD27A", 150 + 40 * math.sin(t * 9)), col("#FFD27A", 0)]))
        cv.drawCircle(0, 85, 120, glow)
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-24, 50, 48, 70), 8, 8), P("#FFD27A"))
        cv.restore()
    elif kind == "radio":
        cv.save()
        cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(-50, -40, 100, 70), 10, 10), P("#3B3F4A"))
        cv.drawCircle(-18, -5, 18, P("#9AA3B5")); cv.drawCircle(25, -18, 7, P("#E2B661"))
        cv.drawLine(30, -40, 60, -110, P("#9AA3B5", 255, 5))
        cv.restore()

def draw_hat(cv, kind, t):
    """Hat frame: (0,0) = top of the head between the ear tufts."""
    if kind == "bicorne":
        h = skia.Path(); h.moveTo(-250, 10)
        h.cubicTo(-160, -40, -60, -150, 0, -150); h.cubicTo(60, -150, 160, -40, 250, 10)
        h.cubicTo(120, -20, -120, -20, -250, 10); h.close()
        cv.drawPath(h, grad_paint((0, -150), (0, 10), ["#2A2E3A", "#0E1018"]))
        trim = skia.Path(); trim.moveTo(-250, 10); trim.cubicTo(-160, -40, -60, -150, 0, -150)
        trim.cubicTo(60, -150, 160, -40, 250, 10)
        cv.drawPath(trim, P("#E2B661", 255, 9))
        cv.drawCircle(0, -70, 28, P("#E2B661")); cv.drawCircle(0, -70, 16, P("#1F3A6B"))
    elif kind == "tricorne":
        h = skia.Path(); h.moveTo(-230, 0); h.lineTo(0, -60); h.lineTo(230, 0); h.lineTo(0, -150); h.close()
        cv.drawPath(h, grad_paint((0, -150), (0, 0), ["#2A2420", "#0E0B08"]))
        cv.drawPath(h, P("#D9B36A", 255, 7))
    elif kind == "detective":
        cv.drawOval(skia.Rect.MakeXYWH(-215, -40, 430, 70), P("#5E4A30"))
        dome = skia.Path(); dome.addArc(skia.Rect.MakeXYWH(-170, -170, 340, 300), 180, 180)
        cv.drawPath(dome, grad_paint((0, -170), (0, -20), ["#8A6E48", "#5E4A30"]))
        for k in range(-3, 4):
            cv.drawLine(k * 45, -150 + abs(k) * 6, k * 45, -22, P("#4A3820", 180, 4))
        cv.drawRect(skia.Rect.MakeXYWH(-168, -48, 336, 22), P("#2E2416"))
    elif kind == "headphones":
        band = skia.Path(); band.addArc(skia.Rect.MakeXYWH(-230, -130, 460, 300), 190, 160)
        cv.drawPath(band, P("#3B3F4A", 255, 22))
        for s in (-1, 1):
            cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(s * 235 - 40, -10, 80, 120), 30, 30), P("#3B3F4A"))
            cv.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(s * 235 - 26, 6, 52, 88), 20, 20), P("#E2B661"))
    elif kind == "beret":
        b = skia.Path(); b.addOval(skia.Rect.MakeXYWH(-190, -120, 360, 130))
        cv.drawPath(b, grad_paint((0, -120), (0, 10), ["#B23A2E", "#6E1A14"]))
        cv.drawCircle(-20, -122, 12, P("#6E1A14"))
    elif kind == "crown":
        c = skia.Path(); c.moveTo(-150, 0)
        for k, x in enumerate([-150, -100, -50, 0, 50, 100, 150]):
            c.lineTo(x, -120 if k % 2 == 0 else -50)
        c.lineTo(150, 0); c.close()
        cv.drawPath(c, grad_paint((0, -120), (0, 0), ["#FBE7B0", "#C48D3C"]))
        for x in (-100, 0, 100): cv.drawCircle(x, -40, 14, P("#B23A2E"))

def draw_coat(cv, kind):
    if kind not in COATS:
        return
    c, sh, trim = COATS[kind]
    p = skia.Path()
    p.moveTo(-252, -300)
    p.cubicTo(-200, -330, -120, -340, -70, -330)
    p.lineTo(0, -230); p.lineTo(70, -330)
    p.cubicTo(120, -340, 200, -330, 252, -300)
    p.cubicTo(258, -200, 250, -80, 160, -30)
    p.cubicTo(100, -14, -100, -14, -160, -30)
    p.cubicTo(-250, -80, -258, -200, -252, -300); p.close()
    cv.drawPath(p, grad_paint((0, -340), (0, -14), [c, sh]))
    cv.drawPath(p, P(OUTLINE, 255, 6))
    # lapels + buttons
    for s in (-1, 1):
        lp = skia.Path(); lp.moveTo(s * 70, -330); lp.lineTo(0, -230); lp.lineTo(s * 40, -170); lp.lineTo(s * 105, -300); lp.close()
        cv.drawPath(lp, P(sh)); cv.drawPath(lp, P(trim, 255, 4))
    for k in range(3):
        for s in (-1, 1):
            cv.drawCircle(s * 34, -175 + k * 50, 9, P(trim))
    if kind == "navy":   # epaulettes
        for s in (-1, 1):
            cv.drawOval(skia.Rect.MakeXYWH(s * 205 - 50, -335, 100, 34), P(trim))
            for k in range(6):
                cv.drawLine(s * 205 - 40 + k * 16, -305, s * 205 - 40 + k * 16, -282, P(trim, 255, 5))

def draw_owl(cv, t, e=0.0, costume=None, look=(0, -0.5), surprise=0.0, blink=0.0, point=0.0, mood="neutral"):
    costume = costume or {}
    ruff = 1 + 0.04 * surprise
    # shadow
    sh = skia.Paint(); sh.setShader(skia.GradientShader.MakeRadial(center=(0, 0), radius=280,
            colors=[col("#000000", 150), col("#000000", 0)]))
    cv.save(); cv.scale(1, .16); cv.drawCircle(0, 0, 280, sh); cv.restore()
    # feet
    for s in (-1, 1):
        for k in (-1, 0, 1):
            cv.drawLine(s * 70, -26, s * 70 + k * 26, -2, P("#E39A3B", 255, 16))
    # left wing (behind, holding the quill)
    la = 8 + 5 * math.sin(t * 1.6)
    cv.save(); cv.translate(-225, -330); cv.rotate(la)
    wp = wing_path(-1)
    cv.drawPath(wp, grad_paint((0, 0), (0, 250), [FEATHER_MID, FEATHER_BOT]))
    cv.drawPath(wp, P(OUTLINE, 255, 6))
    draw_quill(cv, -70, 210, -18 + 6 * math.sin(t * 1.3), .95)
    cv.restore()
    # right wing (gestures / points)
    ra = -10 - 120 * point + 6 * math.sin(t * 3.1)
    cv.save(); cv.translate(225, -330); cv.rotate(ra)
    wp = wing_path(1)
    cv.drawPath(wp, grad_paint((0, 0), (0, 250), [FEATHER_MID, FEATHER_BOT]))
    cv.drawPath(wp, P(OUTLINE, 255, 6))
    if costume.get("accessory"):
        cv.save(); cv.translate(60, 225); cv.rotate(-ra * .6)
        draw_accessory(cv, costume["accessory"], t)
        cv.restore()
    cv.restore()
    # body
    cv.save(); cv.scale(ruff, 1)
    body = owl_body_path()
    cv.drawPath(body, grad_paint((0, -650), (0, -14), [FEATHER_TOP, FEATHER_MID, FEATHER_BOT], [0, .55, 1]))
    cv.drawPath(body, P(OUTLINE, 255, 7))
    cv.restore()
    # belly with feather scallops
    belly = skia.Path(); belly.addOval(skia.Rect.MakeXYWH(-165, -360, 330, 330))
    cv.drawPath(belly, grad_paint((0, -360), (0, -30), [BELLY, "#D6B47A"]))
    for row in range(5):
        y = -300 + row * 55
        n = 5 - abs(row - 2) // 2
        for k in range(-n, n + 1):
            x = k * 48 + (24 if row % 2 else 0)
            if x * x / 150 ** 2 + (y + 195) ** 2 / 160 ** 2 < 1:
                arc = skia.Path(); arc.addArc(skia.Rect.MakeXYWH(x - 20, y - 14, 40, 30), 20, 140)
                cv.drawPath(arc, P("#A9834C", 255, 4))
    draw_coat(cv, costume.get("coat"))
    # facial disc
    for s in (-1, 1):
        cv.drawCircle(s * 92, -440, 118, P(FACE))
    cv.drawCircle(0, -400, 70, P(FACE))
    for s in (-1, 1):
        cv.drawCircle(s * 92, -440, 118, P("#C9A46C", 255, 4))
    # eyes
    eye_r = 72 * (1 + .12 * surprise)
    for s in (-1, 1):
        x, y = s * 92, -445
        cv.drawCircle(x, y, eye_r, P("#FFFFFF"))
        iris = skia.Paint(); iris.setShader(skia.GradientShader.MakeRadial(center=(x, y), radius=50,
               colors=[col("#FFE08A"), col("#E9A73A"), col("#B06A18")], positions=[0, .6, 1]))
        px, py = x + look[0] * 16, y + look[1] * 14
        cv.drawCircle(px, py, 48, iris)
        cv.drawCircle(px, py, 25 * (1 - .3 * surprise), P("#120C08"))
        cv.drawCircle(px + 13, py - 14, 10, P("#FFFFFF"))
        cv.drawCircle(px - 10, py + 12, 4, P("#FFFFFF", 200))
        if blink > 0.01:   # eyelids
            hgt = eye_r * 2 * blink
            cv.save()
            clip = skia.Path(); clip.addCircle(x, y, eye_r)
            cv.clipPath(clip, doAntiAlias=True)
            cv.drawRect(skia.Rect.MakeXYWH(x - eye_r, y - eye_r, eye_r * 2, hgt), P(FEATHER_TOP))
            cv.drawLine(x - eye_r, y - eye_r + hgt, x + eye_r, y - eye_r + hgt, P(OUTLINE, 255, 5))
            cv.restore()
        # spectacles
        cv.drawCircle(x, y, eye_r + 14, P("#E2B661", 255, 11))
        cv.drawCircle(x, y, eye_r + 14, P("#8A5A22", 255, 3))
        # brow feathers
        by = y - eye_r - 34 - 26 * surprise - 10 * e
        # inner end of the brow (toward the beak) moves with the mood
        tilt = {"worried": -22, "serious": 22, "happy": -6, "surprised": -10}.get(mood, 0)
        inner_x, outer_x = x - 48 * s, x + 48 * s
        brow = skia.Path(); brow.moveTo(inner_x, by + 10 + tilt)
        brow.quadTo(x, by - 22 - 8 * surprise, outer_x, by + 10 - tilt * .3)
        cv.drawPath(brow, P(FEATHER_BOT, 255, 15))
        if mood == "happy" and blink < .5:   # smiling lower lids
            cv.save(); clip = skia.Path(); clip.addCircle(x, y, eye_r); cv.clipPath(clip, doAntiAlias=True)
            cv.drawOval(skia.Rect.MakeXYWH(x - eye_r * 1.3, y + eye_r * .35, eye_r * 2.6, eye_r * 1.4), P(FACE))
            cv.restore()
            arc = skia.Path(); arc.addArc(skia.Rect.MakeXYWH(x - eye_r * .9, y + eye_r * .25, eye_r * 1.8, eye_r * .8), 200, 140)
            cv.drawPath(arc, P(OUTLINE, 255, 4))
    cv.drawLine(-12, -445, 12, -445, P("#E2B661", 255, 9))
    # beak (lip-sync)
    op = max(e, .5 * surprise)
    cv.save(); cv.translate(0, -392)
    upper = skia.Path(); upper.moveTo(-30, -14); upper.quadTo(0, -34, 30, -14); upper.lineTo(0, 48); upper.close()
    if op > .05:
        mouth = skia.Path(); mouth.moveTo(-24, 0); mouth.lineTo(24, 0); mouth.lineTo(0, 30 + 60 * op); mouth.close()
        cv.drawPath(mouth, P("#5A1A10"))
        tongue = skia.Path(); tongue.addOval(skia.Rect.MakeXYWH(-12, 18 + 30 * op, 24, 20 * op + 4))
        cv.drawPath(tongue, P("#D9544A"))
    lower = skia.Path(); lower.moveTo(-20, 8 + 40 * op); lower.lineTo(20, 8 + 40 * op); lower.lineTo(0, 44 + 64 * op); lower.close()
    cv.drawPath(lower, P("#C77A22")); cv.drawPath(lower, P(OUTLINE, 255, 4))
    cv.drawPath(upper, grad_paint((0, -34), (0, 48), ["#F5B24A", "#C77A22"])); cv.drawPath(upper, P(OUTLINE, 255, 4))
    cv.restore()
    # cheeks
    for s in (-1, 1):
        g = skia.Paint(); g.setShader(skia.GradientShader.MakeRadial(center=(s * 150, -350), radius=40,
              colors=[col("#E8705A", 110), col("#E8705A", 0)])); cv.drawCircle(s * 150, -350, 40, g)
    # hat
    if costume.get("hat"):
        cv.save(); cv.translate(0, -598); draw_hat(cv, costume["hat"], t); cv.restore()
