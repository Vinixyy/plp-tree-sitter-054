import re
import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_KOMENTAR = Query(PY, "((comment) @c)")
POLA_TODO = re.compile(r"\b(TODO|FIXME)\b")
LEWATI = {"venv", ".venv", ".git", "node_modules", "__pycache__"}


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    komentar = QueryCursor(Q_KOMENTAR).captures(tree.root_node).get("c", [])
    for node in komentar:
        teks = node.text.decode(errors="replace")
        if POLA_TODO.search(teks):
            print(f"{path}:{node.start_point[0] + 1}: {teks.strip()}")


def iter_py(folder):
    for path in Path(folder).rglob("*.py"):
        if not LEWATI.intersection(path.parts):
            yield path


if __name__ == "__main__":
    for path in iter_py(sys.argv[1]):
        cek_file(path)
