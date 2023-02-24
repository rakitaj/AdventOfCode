from __future__ import annotations
from typing import Any
import ast


class NestedList:
    def __init__(self, parent: NestedList | None, children: list[NestedList], data: list[int]):
        self.parent = parent
        self.children = children
        self.data = data


def parse_to_nested_list(line: str) -> NestedList:
    root = NestedList(None, list(), list())
    current = root
    i = 0
    while i < len(line):
        if line[i] == "[":
            nl = NestedList(current, list(), list())
            current.children.append(nl)
            current = nl
        elif line[i] == "]" and current.parent is not None:
            current = current.parent
        else:
            number = ""
            while line[i].isdigit():
                number = number + line[i]
                i += 1
            current.data.append(int(number))
        i += 1
    return current


def parse_line(line: str) -> Any:
    x = ast.literal_eval(line)
    return x


def compare_lines(n1: NestedList, n2: NestedList) -> bool:
    while n1 is not None and n2 is not None:
        for i, _ in enumerate(n1.data):
            if len(n1.data) < len(n2.data):
                return False
            if n2.data[i] > n1.data[i]:
                return False
    return True
