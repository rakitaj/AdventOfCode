from src.common.dataload import DataLoader, Answers
from src.common.grid import Grid, Direction

class Day06Answers(Answers):

    def __init__(self) -> None:
        loader = DataLoader(2024, "day06.txt")
        self.lines = loader.readlines_str()
        self.grid = Grid.from_strings_no_spaces(self.lines)

    def part1(self) -> str:
        visited: set[tuple[int, int]] = set()
        start = self.grid.find("^")
        assert start is not None
        x, y = start
        direction = Direction.UP
        while self.grid.try_get(x, y):
            next_char = self.peek(x, y, direction)
            
                
        return str(len(visited))

    def peek(self, x: int, y:int, direction: Direction) -> str | None:
        match direction:
            case Direction.UP:
                return self.grid.get(x, y + 1) if self.grid.try_get(x, y + 1) else None
            case Direction.RIGHT:
                return self.grid.get(x + 1, y) if self.grid.try_get(x + 1, y) else None
            case Direction.DOWN:
                return self.grid.get(x, y - 1) if self.grid.try_get(x, y - 1) else None
            case Direction.LEFT:
                return self.grid.get(x - 1, y) if self.grid.try_get(x - 1, y) else None