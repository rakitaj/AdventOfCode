from typing import Sequence

from src.common.dataload import DataLoader
from src.common.grid import Point


def tail_visited_once(instructions: list[tuple[str, int]]) -> int:
    head = Point(0, 0)
    tail = Point(0, 0)
    visited: set[tuple[int, int]] = {(0, 0)}
    for direction, magnitude in instructions:
        for _ in range(magnitude):
            match direction:
                case "L":
                    head.x -= 1
                case "R":
                    head.x += 1
                case "U":
                    head.y += 1
                case "D":
                    head.y -= 1
            tail = update_tail(head, tail)
            visited.add(tail.to_tuple())
    return len(visited)


def update_tail(head: Point, tail: Point) -> Point:
    diffx = head.x - tail.x
    diffy = head.y - tail.y
    match diffx, diffy:
        case -1 | 0 | 1 as x, -2 | 2 as y:
            tail.x += x
            tail.y = tail.y + (y // 2)
        case -2 | 2 as x, -1 | 0 | 1 as y:
            tail.x = tail.x + (x // 2)
            tail.y += y
    return tail


def parse_data(lines: Sequence[str]) -> list[tuple[str, int]]:
    instructions = list()
    for line in lines:
        direction, magnitue = line.split()
        instructions.append((direction, int(magnitue)))
    return instructions


def part01_answer() -> str:
    loader = DataLoader(2022, "day09.txt")
    data = loader.readlines_str()
    instructions = parse_data(data)
    result = tail_visited_once(instructions)
    return str(result)
