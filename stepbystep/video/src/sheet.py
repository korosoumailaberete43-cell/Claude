"""Planche contact : python3 sheet.py sortie.png img1 img2 ... (3 colonnes)."""
import sys
from PIL import Image, ImageDraw
out, files = sys.argv[1], sys.argv[2:]
w, h = 640, 360
rows = (len(files) + 2) // 3
S = Image.new("RGB", (3 * w, rows * h), (90, 90, 90))
for i, f in enumerate(files):
    im = Image.open(f).convert("RGB").resize((w, h), Image.LANCZOS)
    d = ImageDraw.Draw(im)
    lab = f.rsplit("_", 1)[-1].replace(".png", "")
    d.rectangle((0, 0, 70, 26), fill=(0, 0, 0)); d.text((6, 6), lab, fill=(255, 255, 255))
    S.paste(im, ((i % 3) * w, (i // 3) * h))
S.save(out)
