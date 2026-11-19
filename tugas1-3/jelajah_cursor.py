import sys

import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))


def jelajah(cursor, kedalaman=0):
    node = cursor.node
    baris, kolom = node.start_point
    field = cursor.field_name
    label = f"{field}: " if field else ""
    print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")

    if cursor.goto_first_child():
        while True:
            if cursor.node.is_named:
                jelajah(cursor, kedalaman + 1)
            if not cursor.goto_next_sibling():
                break
        cursor.goto_parent()


with open(sys.argv[1], "rb") as f:
    tree = parser.parse(f.read())

jelajah(tree.walk())
