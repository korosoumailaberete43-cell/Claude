"""Convertit les affiches 9x16 en JPEG pour TikTok (mode photo) et Metricool.

python3 tiktok.py            → toutes les publications présentes dans out/
python3 tiktok.py J15 TE20   → seulement celles dont l'identifiant commence par…
"""
import pathlib
import sys

from PIL import Image

OUT = pathlib.Path(__file__).resolve().parent / "out"


def main():
    prefixes = sys.argv[1:]
    n = 0
    for d in sorted(OUT.iterdir()):
        src = d / "9x16"
        if not src.is_dir() or (prefixes and not any(d.name.startswith(p) for p in prefixes)):
            continue
        dest = d / "tiktok"
        dest.mkdir(exist_ok=True)
        for f in sorted(src.glob("*.png")):
            Image.open(f).convert("RGB").save(dest / f"{f.stem}.jpg", quality=92, optimize=True)
            n += 1
    print(f"{n} affiches converties")


if __name__ == "__main__":
    main()
