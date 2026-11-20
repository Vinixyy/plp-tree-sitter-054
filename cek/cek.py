import re
import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_KOMENTAR = Query(PY, "((comment) @c)")
Q_FUNGSI = Query(PY, "(function_definition name: (identifier) @nama) @fungsi")
POLA_TODO = re.compile(r"\b(TODO|FIXME)\b")
LEWATI = {"venv", ".venv", ".git", "node_modules", "__pycache__"}


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    komentar = QueryCursor(Q_KOMENTAR).captures(tree.root_node).get("c", [])
    for node in komentar:
        teks = node.text.decode(errors="replace")
        if POLA_TODO.search(teks):
            print(f"{path}:{node.start_point[0] + 1}: {teks.strip()}")

    # Fitur 2: fungsi lebih dari 30 baris
    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        nama = cap["nama"][0].text.decode()
        fungsi = cap["fungsi"][0]
        jumlah = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if jumlah > 30:
            print(
                f"{path}:{fungsi.start_point[0] + 1}: "
                f"fungsi {nama} ({jumlah} baris)"
            )

    # Fitur 3: file dengan error sintaks
    if tree.root_node.has_error:
        node = cari_error(tree.root_node)
        if node is not None:
            print(f"{path}:{node.start_point[0] + 1}: error pada {node.type}")


def cari_error(node):
    if node.is_error or node.is_missing:
        return node
    for child in node.children:
        hasil = cari_error(child)
        if hasil is not None:
            return hasil
    return None


def iter_py(folder):
    for path in Path(folder).rglob("*.py"):
        if not LEWATI.intersection(path.parts):
            yield path


if __name__ == "__main__":
    for path in iter_py(sys.argv[1]):
        cek_file(path)
