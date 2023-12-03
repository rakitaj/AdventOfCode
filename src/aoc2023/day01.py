from src.common.dataload import DataLoader

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def load_and_parse() -> list[str]:
    loader = DataLoader(2023, "day01.txt")
    return loader.readlines_str()


def parse_digits(s: str) -> int:
    first = -1
    last = -1
    for c in s:
        if c.isdigit():
            num = int(c)
            if first == -1:
                first = num
            last = num
    return (first * 10) + last


def try_parse_digit(s: str, i: int) -> tuple[bool, int, int]:
    if s[i].isdigit():
        return (True, int(s[i]), 1)
    for key, value in digits.items():
        if s[i::].startswith(key):
            return (True, value, len(key))
    return (False, -1, -1)


def parse_string_digits(s: str) -> int:
    first = -1
    last = -1
    i = 0
    while i < len(s):
        parsed, num, skipahead = try_parse_digit(s, i)
        if parsed:
            if first == -1:
                first = num
            last = num
            i += skipahead
        else:
            i += 1
    return (first * 10) + last


def part01_answer() -> str:
    strings = load_and_parse()
    total = 0
    for s in strings:
        num = parse_digits(s)
        total += num
    return str(total)


def part02_answer() -> str:
    """
    54718 - too high
    """
    strings = load_and_parse()
    total = _part02_answer(strings)
    return str(total)


def _part02_answer(strings: list[str]) -> int:
    total = 0
    for s in strings:
        num = parse_string_digits(s)
        total += num
    return total
