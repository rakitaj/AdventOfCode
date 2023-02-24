from typing import Any
from src.aoc2022.day13 import parse_line, parse_to_nested_list, NestedList
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


@pytest.mark.parametrize("line, expected", [("[1,1,3,1,1]", [1, 1, 3, 1, 1])])
def test_parse_line(line: str, expected: Any):
    actual = parse_line(line)
    assert actual == expected


def test_parse_to_nested_list():
    line = "[1,1,3,1,1]"
    expected = NestedList(None, list(), [1, 1, 3, 1, 1])
    actual = parse_to_nested_list(line)
    assert expected.data == actual.data
