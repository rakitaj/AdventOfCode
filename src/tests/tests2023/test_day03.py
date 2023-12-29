import pytest
from src.aoc2023.day03 import part_numbers, symbol_adjacent, part_numbers_all_lines, gear_numbers

sample_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

sample_data_long = """...788.............................54.........501...........555.........270.................................521......893....................
..../..*963........................*..860......................*....53...../.....................52.................&....347........428*522.""".splitlines()

sample_data_2 = """12.......*..
+.........34
.......-12..
..78........
..*....60...
78.........9
.5.....23..$
8...90*12...
............
2.2......12.
.*.........*
1.1..503+.56""".splitlines()


def test_part_numers_with_sample_data():
    numbers = part_numbers(None, sample_data[0], sample_data[1])
    assert numbers == [467]


@pytest.mark.parametrize("num_range, symbols, expected", [((3, 7), [2, 10], True)])
def test_symbol_adjacent(num_range: tuple[int, int], symbols: list[int], expected: bool):
    assert symbol_adjacent(num_range, symbols) == expected


@pytest.mark.parametrize("data_var, expected", [(sample_data, 4361), (sample_data_2, 925)])
def test_part_numbers_sample_data(data_var: list[str], expected: int):
    actual = part_numbers_all_lines(data_var)
    assert actual == expected


def test_part_numbers_sample_data_long():
    actual = part_numbers_all_lines(sample_data_long)
    assert actual == sum([788, 54, 555, 270, 893, 963, 428, 522])


def test_part_numbers_eol_does_not_count():
    actual = part_numbers_all_lines(["123..........45*..6\n"])
    assert actual == 45


@pytest.mark.skip
def test_gear_numbers_sample_data():
    actual = gear_numbers(sample_data[0], sample_data[1], sample_data_2[2])
    assert actual == 45
