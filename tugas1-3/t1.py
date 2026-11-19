import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

for path in sys.argv[1:]:
    print(f"=== {path} ===")
    tree = parser.parse(open(path, "rb").read())
    print(tree.root_node)