from collections import deque
from src.aoc2022.day05 import find_quantity, populate_stacks, parse_lines, execute_instructions


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
    assert result[0] == deque(["Z", "N"])
    assert result[1] == deque(["M", "C", "D"])


def test_puzzle_flow():
    lines = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines()
    stacks_and_instructions = parse_lines(lines)
    actual = execute_instructions(stacks_and_instructions)
    assert actual == ["C", "M", "Z"]
