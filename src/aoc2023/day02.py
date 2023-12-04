import re
from dataclasses import dataclass
from src.common.dataload import DataLoader


# "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
game_pattern = re.compile(r"Game (\d+)")
red_pattern = re.compile(r"(\d+) red")
green_pattern = re.compile(r"(\d+) green")
blue_pattern = re.compile(r"(\d+) blue")


@dataclass
class CubeCounts:
    red: int
    green: int
    blue: int


def is_game_possible(max_cubes: CubeCounts, game: CubeCounts) -> bool:
    return (max_cubes.red >= game.red) and (max_cubes.green >= game.green) and (max_cubes.red >= game.red)


def parse_and_test_line(line: str, predicate: CubeCounts) -> bool:
    reds = red_pattern.findall(line)
    greens = green_pattern.findall(line)
    blues = blue_pattern.findall(line)
    for red in reds:
        red_num = int(red)
        if red_num > predicate.red:
            return False
    for green in greens:
        green_num = int(green)
        if green_num > predicate.green:
            return False
    for blue in blues:
        blue_num = int(blue)
        if blue_num > predicate.blue:
            return False
    return True


def min_cubes_line(line: str) -> CubeCounts:
    reds = red_pattern.findall(line)
    greens = green_pattern.findall(line)
    blues = blue_pattern.findall(line)
    red_nums: list[int] = list()
    blue_nums: list[int] = list()
    green_nums: list[int] = list()
    for red in reds:
        red_nums.append(int(red))
    for green in greens:
        green_nums.append(int(green))
    for blue in blues:
        blue_nums.append(int(blue))
    cube_counts = CubeCounts(max(red_nums), max(green_nums), max(blue_nums))
    return cube_counts


def part01_answer():
    loader = DataLoader(2023, "day02.txt")
    lines = loader.readlines_str()
    total = 0
    predicate = CubeCounts(12, 13, 14)
    for line in lines:
        game_id_match = game_pattern.search(line)
        if parse_and_test_line(line, predicate):
            assert game_id_match is not None
            total += int(game_id_match.group(1))
    return total


def part02_answer():
    loader = DataLoader(2023, "day02.txt")
    lines = loader.readlines_str()
    total = 0
    for line in lines:
        min_cubes = min_cubes_line(line)
        power = min_cubes.blue * min_cubes.green * min_cubes.red
        total += power
    return total
