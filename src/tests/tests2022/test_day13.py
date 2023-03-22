from src.aoc2022.day13 import compare_lines, NestedList, parse
import pytest

small_data = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


@pytest.mark.parametrize(
    "line1, line2, expected",
    [
        ("[1,1,3,1,1]", "[1,1,5,1,1]", True),
        ("[[1], [2, 3, 4]]", "[[1], 4]", True),
        ("[9]", "[[8,7,6]]", False),
    ],
)
def test_compare_lines(line1: str, line2: str, expected: bool):
    assert compare_lines(line1, line2) is expected


def test_parse_line_1():
    actual = parse("[1,1,3,1,1]")
    assert actual.parent is None
    assert len(actual.children) == 0
    assert actual.data == [1, 1, 3, 1, 1]


def test_parse_line_2():
    actual = parse("[[1],[2,3,4]]")
    assert actual.parent is None
    assert len(actual.children) == 2
    assert actual.children[0].data == [1]
    assert actual.children[1].data == [2, 3, 4]


def test_parse_line_3():
    actual = parse("[[[]]]")
    assert actual.parent is None
    assert len(actual.children) == 1
    assert actual.children[0].children[0].data == []
