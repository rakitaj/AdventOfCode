from __future__ import annotations
import ast

# class NestedList:
#     def __init__(self, parent: NestedList | None, children: list[NestedList] | None, data: list[int]):
#         self.parent = parent
#         self.child = children
#         self.data = data


# def parse_line(line: str) -> NestedList:
#     root = NestedList(None, None, list())
#     while i := 0 < len(line):
#         if line[i] == "[":
#             i += i
#     return root


def parse_line(line: str) -> ast.AST:
    x = ast.literal_eval(line)
    return x
