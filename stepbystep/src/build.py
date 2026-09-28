"""python3 build.py [numéros de pages...] — génère, rend en PDF et prévisualise en PNG."""
import os, pathlib, subprocess, sys
import pymupdf
import pages_a
try:
    import pages_b
    ALL = pages_a.PAGES + pages_b.PAGES
except ImportError:
    ALL = pages_a.PAGES
OUT = pathlib.Path(__file__).resolve().parent.parent / "out" / "pages"
OUT.mkdir(parents=True, exist_ok=True)
sel = [int(a) for a in sys.argv[1:]] or list(range(1, len(ALL) + 1))
files = []
for n in sel:
    f = OUT / f"page_{n:02d}.html"
    f.write_text(ALL[n - 1](), encoding="utf-8")
    files.append(str(f))
env = dict(os.environ, NODE_PATH=subprocess.check_output(["npm", "root", "-g"], text=True).strip())
subprocess.run(["node", str(pathlib.Path(__file__).parent / "render_pdf.js"), *files], check=True, env=env)
for f in files:
    pdf = f.replace(".html", ".pdf")
    d = pymupdf.open(pdf)
    assert len(d) == 1, f"{pdf}: {len(d)} pages"
    d[0].get_pixmap(matrix=pymupdf.Matrix(1.6, 1.6)).save(pdf.replace(".pdf", ".png"))
print("ok", sel)
