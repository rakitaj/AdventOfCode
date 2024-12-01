
from src.aoc2023.day08 import parse


def test_navigate_simple_path():
    lines = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".splitlines()
    navigator = parse(lines)
    assert navigator.path() == 2


def test_navigate_longer_path():
    lines = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()
    navigator = parse(lines)
    assert navigator.path() == 6


def test_navigate_part_2_algo():
    lines = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()
    navigator = parse(lines)
    assert navigator.path2() == 6
