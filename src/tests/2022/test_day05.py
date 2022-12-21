import pytest
from src.aoc2022.day05 import find_quantity, populate_stacks


def test_find_quantity():
    lines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

""".splitlines()
    num_stacks, line_num = find_quantity(lines)
    assert num_stacks == 3
    assert line_num == 4


def test_populate_stacks():
    lines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """.splitlines()
    result = populate_stacks(lines, 3, 4)
    assert result[0] == ["N", "Z"]
