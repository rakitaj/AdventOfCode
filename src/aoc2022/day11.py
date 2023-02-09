import re
import parse
from typing import Callable


class Monkey:
    def __init__(
        self,
        id_num: int,
        starting_items: list[int],
        op: Callable[[int], int],
        test: Callable[[int], bool],
        true_dest: int,
        false_dest: int,
    ):
        self.id_num = id_num
        self.items = starting_items
        self.op = op
        self.test = test
        self.true_dest = true_dest
        self.false_dest = false_dest


def parse_starting_items(line: str) -> list[int]:
    matched_ints = re.findall(r"(\d+)", line)
    starting_items: list[int] = [int(x) for x in matched_ints]
    return starting_items


def parse_op(line: str) -> Callable[[int], int]:
    parts = line.split("=")
    left_expr, op, right_expr = parts[1].split()
    match left_expr, op, right_expr:
        case ["old", "+", "old"]:
            return lambda x: x + x
        case ["old", "*", "old"]:
            return lambda x: x * x
        case ["old", "+", right_expr]:
            return lambda x: x + int(right_expr)
        case ["old", "*", right_expr]:
            return lambda x: x * int(right_expr)
        case [left_expr, "+", "old"]:
            return lambda x: int(left_expr) + x
        case [left_expr, "*", "old"]:
            return lambda x: int(left_expr) * x
        case [left_expr, "+", right_expr]:
            return lambda x: int(left_expr) + int(right_expr)
        case [left_expr, "*", right_expr]:
            return lambda x: int(left_expr) * int(right_expr)
    raise ValueError("Can't parse the operation line")


def parse_num(line: str) -> int:
    num_pattern = re.compile(r"(\d+)")
    m = num_pattern.search(line)
    if m is None:
        raise ValueError(m)
    num = int(m.group(0))
    return num


def parse_to_monkey(data: list[str]) -> Monkey:
    parsed_id = parse_num(data[0])
    parsed_starting_items = parse_starting_items(data[1])
    parsed_op = parse_op(data[2])

    test_num = parse_num(data[3])
    parsed_test = lambda x: x % test_num == 0

    left_dest_num = parse_num(data[4])
    right_dest_num = parse_num(data[5])

    monkey = Monkey(parsed_id, parsed_starting_items, parsed_op, parsed_test, left_dest_num, right_dest_num)
    return monkey


def parse_data(data: list[str]) -> list[Monkey]:
    monkeys: list[Monkey] = list()
    for i in range(0, len(data), 7):
        monkey = parse_to_monkey(data[i : i + 6])
        monkeys.append(monkey)
    return monkeys
