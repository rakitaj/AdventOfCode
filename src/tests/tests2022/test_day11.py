from src.aoc2022.day11 import parse_to_monkey, Monkey

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
    assert monkey.test(23) is True
    assert monkey.true_dest == 2 and monkey.false_dest == 3
