import re

integer_pattern = re.compile(r"(\d+)")


def extract_integer(string: str) -> int | None:
    matches = integer_pattern.search(string)
    if isinstance(matches, re.Match):
        return int(matches[0])
    return None


def extract_integers(string: str) -> list[int] | None:
    matches = integer_pattern.findall(string)
    integers = [int(m) for m in matches]
    return integers
