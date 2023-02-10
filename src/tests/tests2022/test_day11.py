from src.aoc2022.day11 import parse_to_monkey, Monkey, parse_data, tick, tick2
from src.common.dataload import DataLoader

one_monkey = """  Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3"""


def test_parse_monkey_text():
    monkey_lines = one_monkey.splitlines()
    monkey = parse_to_monkey(monkey_lines)
    assert monkey.id_num == 0
    assert monkey.items == [79, 98]
    assert monkey.op(2) == 38
    assert monkey.divisor == 23
    assert monkey.true_dest == 2 and monkey.false_dest == 3


def test_small_data_one_round():
    """
    Monkey 0: 20, 23, 27, 26
    Monkey 1: 2080, 25, 167, 207, 401, 1046
    Monkey 2:
    Monkey 3:
    """
    loader = DataLoader(2022, "day11-small.txt")
    small_data = loader.readlines_str()
    monkeys = parse_data(small_data)
    monkeys = tick(monkeys)
    assert monkeys[0].items == [20, 23, 27, 26]
    assert monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
    assert monkeys[2].items == []
    assert monkeys[3].items == []


def test_small_data_twenty_rounds():
    """
    Monkey 0: 10, 12, 14, 26, 34
    Monkey 1: 245, 93, 53, 199, 115
    Monkey 2:
    Monkey 3:
    """
    loader = DataLoader(2022, "day11-small.txt")
    small_data = loader.readlines_str()
    monkeys = parse_data(small_data)
    for _ in range(20):
        monkeys = tick(monkeys)
    assert monkeys[0].items == [10, 12, 14, 26, 34]
    assert monkeys[1].items == [245, 93, 53, 199, 115]
    assert monkeys[2].items == []
    assert monkeys[3].items == []
    assert monkeys[0].count == 101 and monkeys[3].count == 105


def test_small_data_tick2():
    loader = DataLoader(2022, "day11-small.txt")
    small_data = loader.readlines_str()
    monkeys = parse_data(small_data)
    for _ in range(20):
        monkeys = tick2(monkeys)
    assert (
        monkeys[0].count == 99
        and monkeys[1].count == 97
        and monkeys[2].count == 8
        and monkeys[3].count == 103
    )
