import re

integer_pattern = re.compile(r"(\d+)")


def extract_integer(string: str) -> int | None:
    matches = integer_pattern.search(string)
    match type(matches):
        case re.Match:
            integer = int(matches[0])
            return integer
        case _:
            return None
