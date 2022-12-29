from src.common.grid import Point
from src.aoc2022.day09 import update_tail, parse_data, tail_visited_once

tiny_data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()


def test_update_tail():
    p1 = Point(5, 0)
    p2 = Point(3, 0)
    p3 = update_tail(p1, p2)
    assert p2 is p3
    assert p2.x == 4 and p2.y == 0


def test_move_rope():
    instructions = parse_data(tiny_data)
    result = tail_visited_once(instructions)
    assert result == 13
