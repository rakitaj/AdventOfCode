from src.common.grid import Point, points_between


class Cave:
    def __init__(self, rocks_set: set[Point]):
        self.rocks = rocks_set
        self.sand: set[Point] = set()

    def tick(self) -> bool:
        """
        Introduce sand at Point(500, 0) and simulate it falling
        until it either comes to rest or falls off the edge of
        the cave.

        Return true if the sand stays in the cave. False if it falls
        off the edge. This lets you run the simulation until false.
        """
        edge_point = max(self.rocks, key=lambda p: p.y)
        current = Point(500, 0)
        while (
            (current + Point(0, 1) not in self.rocks)
            and (current + Point(-1, 1) not in self.rocks)
            and (current + Point(1, 1) not in self.rocks)
        ):
            if current + Point(0, 1) in self.rocks:
                if current + Point(-1, 1) not in self.rocks:
                    current = current + Point(-1, 1)
                    continue
                if current + Point(1, 1) not in self.rocks:
                    current = current + Point(1, 1)
                    continue
            else:
                current = current + Point(0, 1)
                if edge_point.y < current.y:
                    return False
        return True


def parse_line(line: str) -> list[Point]:
    result = list()
    split_on_arrow = line.split("->")
    for part in split_on_arrow:
        x, y = part.split(",")
        point = Point(int(x), int(y))
        result.append(point)
    return result
