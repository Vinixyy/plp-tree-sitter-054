import re
import sys
from pathlib import Path

import tree_sitter_javascript as tsjavascript
from tree_sitter import Language, Parser, Query, QueryCursor

JS = Language(tsjavascript.language())
parser = Parser(JS)

Q_KOMENTAR = Query(JS, "((comment) @c)")
Q_FUNGSI = Query(JS, "(function_declaration name: (identifier) @nama) @fungsi")
POLA_TODO = re.compile(r"\b(TODO|FIXME)\b")
LEWATI = {"node_modules", ".git", "dist", "build"}


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    for node in QueryCursor(Q_KOMENTAR).captures(tree.root_node).get("c", []):
        teks = node.text.decode(errors="replace")
        if POLA_TODO.search(teks):
            print(f"{path}:{node.start_point[0] + 1}: {teks.strip()}")

    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        nama = cap["nama"][0].text.decode()
        fungsi = cap["fungsi"][0]
        jumlah = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if jumlah > 30:
            print(
                f"{path}:{fungsi.start_point[0] + 1}: "
                f"fungsi {nama} ({jumlah} baris)"
            )

    if tree.root_node.has_error:
        print(f"{path}:{tree.root_node.start_point[0] + 1}: file mengandung error")


if __name__ == "__main__":
    for path in Path(sys.argv[1]).rglob("*.js"):
        if not LEWATI.intersection(path.parts):
            cek_file(path)
