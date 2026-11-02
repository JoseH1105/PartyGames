"""Regenera el grafo de código (graphify) de Brindis.

Toda la app vive en index.html, y graphify no analiza el JavaScript que va
dentro de <script>. Este script copia ese JavaScript a .graph-src/index.html.js
conservando los números de línea (las demás líneas quedan en blanco), así que
una línea del grafo es la misma línea en index.html. También copia sw.js.

Uso (desde la raíz del repo):
    python tools/build-graph.py           # actualiza el grafo
    python tools/build-graph.py --full    # lo reconstruye desde cero

Resultado: graphify-out/graph.json, GRAPH_REPORT.md y graph.html.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".graph-src"
OUT = ROOT / "graphify-out"


def extract_scripts():
    lines = (ROOT / "index.html").read_text(encoding="utf-8").split("\n")
    out, inside = [], False
    for line in lines:
        if not inside and re.search(r"<script(\s[^>]*)?>", line) and "src=" not in line:
            inside = True
            after = re.split(r"<script[^>]*>", line, maxsplit=1)[1]
            if "</script>" in after:
                out.append(after.split("</script>")[0])
                inside = False
            else:
                out.append(after)
            continue
        if inside and "</script>" in line:
            out.append(line.split("</script>")[0])
            inside = False
            continue
        out.append(line if inside else "")
    SRC.mkdir(exist_ok=True)
    (SRC / "index.html.js").write_text("\n".join(out), encoding="utf-8")
    shutil.copy2(ROOT / "sw.js", SRC / "sw.js")


def graphify(*args):
    subprocess.run([sys.executable, "-m", "graphify", *args], check=True, cwd=ROOT)


def main():
    full = "--full" in sys.argv
    extract_scripts()
    # graphify escribe en .graph-src/graphify-out; se reutiliza como caché
    if full or not (SRC / "graphify-out" / "graph.json").exists():
        graphify("extract", str(SRC), "--code-only")
    else:
        graphify("update", str(SRC), "--force")
    graphify("cluster-only", str(SRC), "--no-label")
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(SRC / "graphify-out", OUT, ignore=shutil.ignore_patterns("cache"))
    print(f"Grafo listo en {OUT}")


if __name__ == "__main__":
    main()
