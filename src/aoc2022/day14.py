# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
from src.common.grid import Point


def parse_line(line: str) -> list[Point]:
    result = list()
    split_on_arrow = line.split("->")
    for part in split_on_arrow:
        x, y = part.split(",")
        point = Point(int(x), int(y))
        result.append(point)
    return result


def rocks_model(nested_points_list: list[list[Point]]) -> set[Point]:
    rocks: set[Point] = set()
    for points_list in nested_points_list:
        for i in range(len(points_list) - 1):
            start = points_list[i]
            end = points_list[i + 1]
