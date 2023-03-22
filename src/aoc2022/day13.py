from __future__ import annotations


class NestedList:
    def __init__(self, parent: NestedList | None, children: list[NestedList], data: list[int]) -> None:
        self.parent = parent
        self.children = children
        self.data = data

    def at_end(self, i: int) -> bool:
        return i >= len(self.data) and self.children is None


def parse(line: str) -> NestedList:
    root = NestedList(None, [], [])
    current = root
    i = 0
    while i < len(line):
        e = line[i]
        if e.isdigit():
            digit = e
            while peek_is_digit(line, i):
                digit += line[i + 1]
                i += 1
            current.data.append(int(digit))
        elif e == "[":
            nl = NestedList(current, [], [])
            current.children.append(nl)
            current = nl
        elif e == "]" and isinstance(current.parent, NestedList):
            current = current.parent
        i += 1
    root.children[0].parent = None
    return root.children[0]


def peek_is_digit(line: str, i: int) -> bool:
    return i + 1 < len(line) and line[i + 1].isdigit()


def compare_lines(line1: str, line2: str) -> bool:
    parsed_1 = parse(line1)
    parsed_2 = parse(line2)
    return compare_lines_recurse(parsed_1, 0, parsed_2, 0)


def compare_lines_recurse(nl1: NestedList, i: int, nl2: NestedList, j: int) -> bool:
    return True
