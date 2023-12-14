import pytest
from src.aoc2023.day05 import OffsetMapping, parse

test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()


@pytest.mark.parametrize(
    "source_n, expected",
    [(0, 0), (48, 48), (50, 52), (96, 98), (98, 50), (99, 51), (79, 81), (14, 14), (55, 57), (13, 13)],
)
def test_offset_mapping_1(source_n: int, expected: int):
    mappings = [(50, 98, 2), (52, 50, 48)]
    offset_mapping = OffsetMapping(mappings)
    assert offset_mapping.calculate(source_n) == expected


def test_parsing_to_seed_optimizer():
    seed_optimizer = parse(test_data)
    assert seed_optimizer.seeds == [79, 14, 55, 13]
    assert seed_optimizer.seed_to_soil.offset_ranges == [(50, 98, 2), (52, 50, 48)]


@pytest.mark.parametrize("seed_num, expected", [(79, 82), (14, 43), (55, 86), (13, 35), (82, 46)])
def test_finding_location(seed_num: int, expected: int):
    seed_optimizer = parse(test_data)
    location = seed_optimizer.location(seed_num)
    assert location == expected


def test_finding_location_from_ranges():
    seed_optimizer = parse(test_data)
    location = seed_optimizer.location_from_ranges()
    assert location == 46
