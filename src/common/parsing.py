import re

integer_pattern = re.compile(r"(\d+)")


def extract_integer(string: str) -> int | None:
    matches = integer_pattern.search(string)
    if isinstance(matches, re.Match):
        return int(matches[0])
    return None
