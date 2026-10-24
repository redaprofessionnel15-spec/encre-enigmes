"""PREVIEW du hibou seul : planche de toutes les humeurs et poses.
python3 owl_sheet.py out.png"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import skia
from character import draw_owl, MOODS, POSES

CELL = 360
combos = [(m, p) for m, p in zip(MOODS, list(POSES) * 2)]
costumes = [dict(hat="bicorne", coat="navy", accessory="spyglass"), dict(hat="detective", coat="brown", accessory="magnifier"),
            dict(hat="beret", coat="red", accessory="lantern"), dict()]
cols = 5; rows = math.ceil(len(combos) / cols)
surf = skia.Surface(cols * CELL, rows * CELL); cv = surf.getCanvas(); cv.clear(skia.Color(18, 27, 54))
font = skia.Font(skia.Typeface("DejaVu Sans"), 20)
for i, (m, p) in enumerate(combos):
    x, y = (i % cols) * CELL, (i // cols) * CELL
    cv.save(); cv.translate(x + CELL / 2, y + CELL - 40); cv.scale(.36, .36)
    draw_owl(cv, 1.0, e=.2, costume=costumes[i % 4], look=(.3, -.4), mood=m, pose=POSES[p])
    cv.restore()
    cv.drawString(f"{m} / {p}", x + 10, y + 26, font, skia.Paint(Color=skia.Color(240, 207, 133), AntiAlias=True))
surf.makeImageSnapshot().save(sys.argv[1], skia.kPNG)
