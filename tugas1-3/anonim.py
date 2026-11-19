import sys

import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

with open(sys.argv[1], "rb") as f:
    tree = parser.parse(f.read())

# children[0] dari module = function_definition pada potongan/fungsi.py
node = tree.root_node.children[0]

print(f"=== anak dari {node.type} ===")
for i, child in enumerate(node.children):
    jenis = "bernama" if child.is_named else "anonim"
    field = node.field_name_for_child(i)
    print(f"{child.type:25} {jenis:8} field={field}")

params = node.child_by_field_name("parameters")
if params is not None:
    print(f"=== isi {params.type} ===")
    for i, child in enumerate(params.children):
        jenis = "bernama" if child.is_named else "anonim"
        print(f"{child.type:25} {jenis:8}")
