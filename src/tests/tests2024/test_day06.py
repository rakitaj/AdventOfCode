from src.aoc2024.day06 import Day06Answers

lines = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()


def test_escape_grid_with_sample_data():
    day6 = Day06Answers()
    day6.set_grid(lines)
    assert day6.part1() == "41"


def test_trap_guard_with_sample_data():
    day6 = Day06Answers()
    day6.set_grid(lines)
    assert day6.part2() == "6"
