from src.common.dataload import DataLoader


def load_and_parse() -> list[tuple[str, str]]:
    loader = DataLoader(2022, "day02.txt")
    data = loader.readlines_str()
    result: list[tuple[str, str]] = list()
    for line in data:
        first, second = line.split()
        result.append((first, second))
    return result


# A, X = Rock
# B, Y = Paper
# C, Z = Scissors
rps_map = {"A": "X", "B": "Y", "C": "Z"}
points_map = {"X": 1, "Y": 2, "Z": 3}


def rock_paper_scissors(opponent: str, me: str) -> int:
    total = 0
    total += points_map[me]
    other = rps_map.get(opponent)
    assert type(other) is str

    diff = ord(me) - ord(other)
    if diff == 0:
        total += 3
    elif diff == 1 or diff == -2:
        total += 6

    return total


def part01_answer() -> str:
    total = 0
    rock_paper_scissors_list = load_and_parse()
    for opponent, me in rock_paper_scissors_list:
        total += rock_paper_scissors(opponent, me)
    return str(total)
