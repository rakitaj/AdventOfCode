import pytest

from src.aoc2022.day07 import FileSystemParser, Lexer, filter_and_sum, lex_instruction

tiny_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()


@pytest.mark.parametrize(
    "instruction, expected",
    [
        ("$ ls", ("command", "ls", "", 1)),
        ("dir a", ("contents", "dir", "a", 1)),
        ("14848514 b.txt", ("contents", "b.txt", "14848514", 1)),
    ],
)
def test_lex_instruction(instruction: str, expected: tuple[str, str, str, int] | None):
    actual = lex_instruction(instruction, 1)
    assert actual == expected


def test_parse_filesystem():
    lexer = Lexer(tiny_data)
    tokens = lexer.lex()
    parser = FileSystemParser(tokens[1:])
    fs = parser.execute()
    assert fs.name == "/"
    assert len(fs.dirs) == 2
    assert len(fs.files) == 2 and fs.files["b.txt"] == 14848514 and fs.files["c.dat"] == 8504156


def test_filter_and_sum():
    lexer = Lexer(tiny_data)
    tokens = lexer.lex()
    parser = FileSystemParser(tokens[1:])
    fs = parser.execute()
    total = filter_and_sum(fs, 0)
    assert total == 95437
