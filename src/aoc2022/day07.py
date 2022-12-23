from __future__ import annotations
from typing import cast
import parse

from src.common.dataload import DataLoader

lex_file = parse.compile("{filesize} {filename}")


class DirNode:
    def __init__(
        self,
        name: str,
        parent: DirNode | None = None,
    ):
        self.name = name
        self.dirs: list[DirNode] = list()
        self.files: dict[str, int] = dict()
        self.parent = parent

    def cd(self, target: str) -> DirNode:
        if target == "..":
            if self.parent is None:
                raise KeyError(f"Node: {self.name} Message: Can't get to parent node")
            return self.parent
        else:
            for dir in self.dirs:
                if dir.name == target:
                    dir.parent = self
                    return dir
        raise KeyError(f"Node: {self.name} Message: Can't get to {target} node")

    def size(self) -> int:
        total = 0
        for _, filesize in self.files.items():
            total += filesize
        for dir in self.dirs:
            total += dir.size()
        return total


class FileSystemParser:
    def __init__(self, tokens: list[tuple[str, str, str, int]]):
        self.tokens = tokens
        self.i = 0

    def at_end(self) -> bool:
        return len(self.tokens) <= self.i

    def peek(self) -> tuple[str, str, str, int] | None:
        if self.at_end() or len(self.tokens) <= (self.i + 1):
            return None
        return self.tokens[self.i + 1]

    def execute(self) -> DirNode:
        root = DirNode("/")
        current_node = root
        while not self.at_end():
            token = self.tokens[self.i]
            if token[0] == "command" and token[1] == "cd":
                current_node = current_node.cd(token[2])
            elif token[0] == "command" and token[1] == "ls":
                pass
            elif token[0] == "contents" and token[1] == "dir":
                current_node.dirs.append(DirNode(token[2], current_node))
            else:
                current_node.files[token[1]] = int(token[2])
            self.i += 1
        return root


def lex_instruction(instruction: str, line_number: int) -> tuple[str, str, str, int]:
    if instruction.startswith("$ cd"):
        cd_to = instruction[5:]
        return ("command", "cd", cd_to, line_number)
    elif instruction.startswith("$ ls"):
        return ("command", "ls", "", line_number)
    elif instruction.startswith("dir"):
        return ("contents", "dir", instruction[4:], line_number)
    else:
        lex_file_result = lex_file.parse(instruction)
        if lex_file_result is None:
            raise ValueError(f"Tried to lex/tokenize filename {instruction} and failed.")
        filename = cast(str, lex_file_result["filename"])
        filesize = cast(str, lex_file_result["filesize"])
        return ("contents", filename, filesize, line_number)


class Lexer:
    def __init__(self, instructions: list[str]):
        self.instructions = instructions

    def lex(self) -> list[tuple[str, str, str, int]]:
        result: list[tuple[str, str, str, int]] = list()
        for i, instruction in enumerate(self.instructions):
            token = lex_instruction(instruction, i + 1)
            if token:
                result.append(token)
        return result


def filter_and_sum(node: DirNode, acc: int) -> int:
    for dir in node.dirs:
        dir_sum = dir.size()
        if dir_sum <= 100000:
            acc += dir_sum
        acc = filter_and_sum(dir, acc)
    return acc


def find_sized_directory(node: DirNode, total_size: int, size_free_target: int) -> int:
    size_used = node.size()
    actual_size_free = total_size - size_used
    needed = size_free_target - actual_size_free

    closest_to_target = size_used

    stack: list[DirNode] = [node]
    while 0 < len(stack):
        current = stack.pop()
        size = current.size()
        if size > needed and size < closest_to_target:
            closest_to_target = size
        for dir in current.dirs:
            stack.append(dir)
    return closest_to_target


def part01_answer() -> str:
    loader = DataLoader(2022, "day07.txt")
    data = loader.readlines_str(True)
    lexer = Lexer(data)
    tokens = lexer.lex()
    parser = FileSystemParser(tokens[1:])
    fs = parser.execute()
    total = filter_and_sum(fs, 0)
    return str(total)


def part02_answer() -> str:
    loader = DataLoader(2022, "day07.txt")
    data = loader.readlines_str(True)
    lexer = Lexer(data)
    tokens = lexer.lex()
    parser = FileSystemParser(tokens[1:])
    fs = parser.execute()
    size = find_sized_directory(fs, 70000000, 30000000)
    return str(size)
