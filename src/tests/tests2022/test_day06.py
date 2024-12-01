import pytest

from src.aoc2022.day06 import ElfPacket


@pytest.mark.parametrize(
    "packet_string, look_ahead, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 4, 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 4, 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 4, 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4, 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4, 11),
    ],
)
def test_elfpacketparser_4(packet_string: str, look_ahead: int, expected: int):
    parser = ElfPacket(packet_string)
    assert parser.start_index(look_ahead) == expected
