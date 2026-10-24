"""Assemble les images PREVIEW en planche : python3 sheet.py dossier_work out.png [colonnes]"""
import sys, glob
from PIL import Image, ImageDraw
fs = sorted(glob.glob(f"{sys.argv[1]}/prev_*.png")); cols = int(sys.argv[3]) if len(sys.argv) > 3 else 7
w, h = 270, 480; S = Image.new("RGB", (w * cols, h * ((len(fs) + cols - 1) // cols)))
for i, f in enumerate(fs):
    S.paste(Image.open(f).resize((w, h)), ((i % cols) * w, (i // cols) * h))
    ImageDraw.Draw(S).text(((i % cols) * w + 6, (i // cols) * h + 4), f[-9:-4] + "s", fill=(255, 80, 80))
S.save(sys.argv[2])
