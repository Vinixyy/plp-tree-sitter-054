import ctypes
import sys

from tree_sitter import Language, Parser

LIB = sys.argv[2] if len(sys.argv) > 2 else "tree-sitter-filter/filter.so"
lib = ctypes.CDLL(LIB)
lib.tree_sitter_filter.restype = ctypes.c_void_p

FILTER = Language(lib.tree_sitter_filter())
parser = Parser(FILTER)

OPS = {"=", "!=", ">", "<", ">=", "<="}
params = []


def nilai(node):
    teks = node.text.decode()
    if node.type == "string":
        return teks[1:-1]
    if node.type == "number":
        return float(teks) if "." in teks else int(teks)
    if node.type == "boolean":
        return teks == "true"
    raise ValueError(f"nilai tidak dikenal: {node.type}")


def sql(node):
    tipe = node.type

    if tipe == "query":
        return sql(node.named_children[0])

    if tipe == "comparison":
        nama = node.child_by_field_name("field").text.decode()
        value = node.child_by_field_name("value")
        op = next((c.type for c in node.children if c.type in OPS), "=")
        params.append(nilai(value))
        return f"{nama} {op} ?"

    if tipe == "and_expression":
        kiri = sql(node.child_by_field_name("left"))
        kanan = sql(node.child_by_field_name("right"))
        return f"({kiri} AND {kanan})"

    if tipe == "or_expression":
        kiri = sql(node.child_by_field_name("left"))
        kanan = sql(node.child_by_field_name("right"))
        return f"({kiri} OR {kanan})"

    if tipe == "not_expression":
        return f"NOT ({sql(node.child_by_field_name('operand'))})"

    if tipe == "parenthesized":
        return f"({sql(node.named_children[0])})"

    if tipe == "in_expression":
        nama = node.child_by_field_name("field").text.decode()
        values = node.child_by_field_name("values")
        for v in values.named_children:
            params.append(nilai(v))
        tanda = ", ".join("?" for _ in values.named_children)
        return f"{nama} IN ({tanda})"

    if tipe == "contains_expression":
        nama = node.child_by_field_name("field").text.decode()
        value = node.child_by_field_name("value")
        params.append(f"%{nilai(value)}%")
        return f"{nama} LIKE ?"

    raise ValueError(f"node tidak dikenal: {tipe}")


source = open(sys.argv[1], "rb").read()
tree = parser.parse(source)

print("WHERE", sql(tree.root_node))
print("PARAMS", params)
