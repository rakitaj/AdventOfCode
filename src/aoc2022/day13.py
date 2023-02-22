from __future__ import annotations
from typing import Any
import ast


# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]


class NestedList:
    def __init__(self, parent: NestedList | None | None, data: list[int]):
        self.parent = parent
        self.data = data


def parse_line_2(line: str) -> NestedList:
    root = NestedList(None, list())
    current = root
    i = 0
    while i < len(line):
        if line[i] == "[":
            child_list = NestedList(current, list())
            current = child_list
        elif line[i] == "]" and current.parent is not None:
            current = current.parent
        else:
            number = ""
            while line[i].
        i += i
    return root


def parse_line(line: str) -> Any:
    x = ast.literal_eval(line)
    return x
