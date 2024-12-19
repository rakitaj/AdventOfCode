from src.common.grid import Grid, Point
from src.common.dataload import Answers, DataLoader

def find_sequence_8_directions(grid: Grid[str], point: Point, sequence: list[str]) -> int:
    found_count = 0
    transforms = Grid.moves()
    for direction in transforms:
        direction_result = _find_sequence_one_direction(grid, point, sequence, direction)
        if direction_result is True:
            found_count += 1
    return found_count

def _find_sequence_one_direction(grid: Grid[str], start: Point, sequence: list[str], transform: tuple[int, int]) -> bool:
    for i, e in enumerate(sequence):
        # Consider i the scaling factor of the transform.
        p = Point(start.x + transform[0] *i, start.y + transform[1] * i)
        if grid.try_get(p.x, p.y) is False or grid.get(p.x, p.y) != e:
            return False
    return True

XMAS = ["X", "M", "A", "S"]

def xmas_cross(grid: Grid[str], p: Point) -> bool:
    if grid.get(p.x, p.y) != 'A':
        return False
    upper_left = grid.try_get(p.x - 1, p.y + 1) and grid.get(p.x - 1, p.y + 1)
    upper_right = grid.try_get(p.x + 1, p.y + 1) and grid.get(p.x + 1, p.y + 1)
    lower_left = grid.try_get(p.x - 1, p.y - 1) and grid.get(p.x - 1, p.y - 1)
    lower_right = grid.try_get(p.x + 1, p.y - 1) and grid.get(p.x + 1, p.y - 1)
    if not all([upper_left, upper_right, lower_left, lower_right]):
        return False
    if mas(upper_left, lower_right) and mas(upper_right, lower_left):
        return True
    return False
    
def mas(char1: str, char2: str) -> bool:
    if char1 == "M" and char2 == "S":
        return True
    if char1 == "S" and char2 == "M":
        return True
    return False

class Day04Answers(Answers):

    def __init__(self):
        loader = DataLoader(2024, "day04.txt")
        self.raw = loader.readlines_str()
        self.grid = Grid.from_strings_no_spaces(self.raw)

    def part1(self) -> str:
        total = 0
        for point in self.grid.iter_points():
            total += find_sequence_8_directions(self.grid, point, XMAS)
        return str(total)

    def part2(self) -> str:
        total = 0
        for point in self.grid.iter_points():
            if xmas_cross(self.grid, point):
                total += 1
        return str(total)
    
    # 578 - too low