from src.common.dataload import DataLoader
from dataclasses import dataclass


@dataclass
class SegmentLocations:
    """Class for keeping track of potentially overlapping segments."""

    a_start: int
    a_end: int
    b_start: int
    b_end: int

    def any_overlap(self) -> bool:
        diff = self.b_start - self.a_end
        return diff <= 0
        # return (
        #     self.start_one in range(self.start_one, self.end_two + 1)
        #     or self.end_one in range(self.start_one, self.end_two + 1)
        #     or self.start_one in range(self.start_one, self.end_one + 1)
        #     or self.end_two in range(self.start_one, self.end_one + 1)
        # )


def load_and_parse() -> list[SegmentLocations]:
    loader = DataLoader(2022, "day04.txt")
    data = loader.readlines_str()
    result: list[SegmentLocations] = list()
    for datum in data:
        pair_one, pair_two = datum.split(",")
        start_one, end_one = pair_one.split("-")
        start_two, end_two = pair_two.split("-")
        result.append(SegmentLocations(int(start_one), int(end_one), int(start_two), int(end_two)))
    return result


def check_overlapping_segments(segment_locations: SegmentLocations) -> int:
    sl = segment_locations
    if sl.a_start <= sl.b_start and sl.b_end <= sl.a_end:
        return 1
    if sl.b_start <= sl.a_start and sl.a_end <= sl.b_end:
        return 1
    return 0


def part01_answer() -> str:
    total = 0
    segment_pairs_list = load_and_parse()
    for segment_pair in segment_pairs_list:
        total += check_overlapping_segments(segment_pair)
    return str(total)


def part02_answer() -> str:
    total = 0
    segment_pairs_list = load_and_parse()
    for segment_pair in segment_pairs_list:
        if segment_pair.any_overlap():
            total += 1
        # total += segment_pair.any_overlap()
    return str(total)
