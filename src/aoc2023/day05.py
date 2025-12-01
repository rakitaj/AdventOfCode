from dataclasses import dataclass
from typing import Sequence

from src.common.dataload import Answers, DataLoader
from src.common.extensions import must
from src.common.parsing import extract_integers


def is_empty_or_whitespace(string: str) -> bool:
    return len(string) == 0 or string.isspace()


@dataclass
class OffsetMapping:
    offset_ranges: list[tuple[int, int, int]]

    def __init__(self, offset_ranges: list[tuple[int, int, int]] | None = None):
        if offset_ranges is None:
            self.offset_ranges = []
        else:
            self.offset_ranges = offset_ranges

    def calculate(self, n: int) -> int:
        for x in self.offset_ranges:
            destination, source, length = x
            if source <= n and n <= source + length:
                return n + (destination - source)
        return n


@dataclass(init=False)
class SeedOptimizer:
    seeds: list[int]
    seed_to_soil: OffsetMapping
    soil_to_fertilizer: OffsetMapping
    fertilizer_to_water: OffsetMapping
    water_to_light: OffsetMapping
    light_to_temperature: OffsetMapping
    temperature_to_humidity: OffsetMapping
    humidity_to_location: OffsetMapping

    def location_from_ranges(self) -> int:
        """Get the seed locations from the seed number ranges."""
        min_seed = 1000000000000000000000000000000
        seeds_length = len(self.seeds)
        for i in range(0, len(self.seeds), 2):
            print(f"{seeds_length} - {i}")
            seed = self.seeds[i]
            length = self.seeds[i + 1]
            for n in range(seed, seed + length):
                location = self.location(n)
                if location < min_seed:
                    min_seed = location
        return min_seed

    def location(self, n: int) -> int:
        """Get the final location of a seed."""
        soil = self.seed_to_soil.calculate(n)
        fertilizer = self.soil_to_fertilizer.calculate(soil)
        water = self.fertilizer_to_water.calculate(fertilizer)
        light = self.water_to_light.calculate(water)
        temperature = self.light_to_temperature.calculate(light)
        humidity = self.temperature_to_humidity.calculate(temperature)
        location = self.humidity_to_location.calculate(humidity)
        return location


def parse(lines: Sequence[str]) -> SeedOptimizer:
    so = SeedOptimizer()
    i = 0
    while i < len(lines):
        if lines[i].startswith("seeds"):
            seeds = must(extract_integers(lines[i]))
            so.seeds = seeds
        if lines[i].startswith("seed-to-soil map"):
            i += 1
            i, so.seed_to_soil = parse_range_offsets(lines, i)
        if lines[i].startswith("soil-to-fertilizer map"):
            i += 1
            i, so.soil_to_fertilizer = parse_range_offsets(lines, i)
        if lines[i].startswith("fertilizer-to-water map"):
            i += 1
            i, so.fertilizer_to_water = parse_range_offsets(lines, i)
        if lines[i].startswith("water-to-light map"):
            i += 1
            i, so.water_to_light = parse_range_offsets(lines, i)
        if lines[i].startswith("light-to-temperature map"):
            i += 1
            i, so.light_to_temperature = parse_range_offsets(lines, i)
        if lines[i].startswith("temperature-to-humidity map"):
            i += 1
            i, so.temperature_to_humidity = parse_range_offsets(lines, i)
        if lines[i].startswith("humidity-to-location map"):
            i += 1
            i, so.humidity_to_location = parse_range_offsets(lines, i)
        i += 1
    return so


def parse_range_offsets(lines: Sequence[str], i: int) -> tuple[int, OffsetMapping]:
    map = OffsetMapping()
    while i < len(lines) and not is_empty_or_whitespace(lines[i]):
        nums = must(extract_integers(lines[i]))
        map.offset_ranges.append(((nums[0], nums[1], nums[2])))
        i += 1
    return (i, map)


class Day05Answers(Answers):
    def __init__(self) -> None:
        loader = DataLoader(2023, "day05.txt")
        self.data = loader.readlines_str()

    def part1(self) -> str:
        seed_optimizer = parse(self.data)
        seed_locations: list[int] = []
        for seed_num in seed_optimizer.seeds:
            location = seed_optimizer.location(seed_num)
            seed_locations.append(location)
        min_seed_location = min(seed_locations)
        return str(min_seed_location)

    def part2(self) -> str:
        return "Ignore"
        seed_optimizer = parse(self.data)
        min_location = seed_optimizer.location_from_ranges()
        return str(min_location)
