from src.common.grid import Grid, Point
from src.common.dataload import Answers, DataLoader

def find_sequence_8_directions[T](grid: Grid[T], point: Point, sequence: list[T]) -> bool:
    transforms = Grid.moves()
    for direction in transforms:
        for i, e in enumerate(sequence):
            point = point + (Point(direction[0], direction[1]) * i)
            # If the point is outside the grid or not equal to the element of the sequence.
            if grid.try_get(point.x, point.y) is False or grid.get(point.x, point.y) != e:
                return False
    return True

class Day04Answers(Answers):

    def __init__(self):
        loader = DataLoader(2024, "day04.txt")
        self.raw = loader.readlines_str()
        self.grid = Grid.from_strings_no_spaces(self.raw)