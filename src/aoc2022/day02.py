from src.common.dataload import DataLoader


def load_and_parse() -> list[tuple[str, str]]:
    loader = DataLoader(2022, "day02.txt")
    data = loader.readlines_str()
    result: list[tuple[str, str]] = list()
    for line in data:
        first, second = line.split()
        result.append((first, second))
    return result


rps_map = {"X": "A", "Y": "B", "Z": "C"}
points_map = {"A": 1, "B": 2, "C": 3}
outcome_map = {"A": 0, "B": 3, "C": 6}
wins = {"A": "B", "B": "C", "C": "A"}
loses = {"A": "C", "B": "A", "C": "B"}


def rock_paper_scissors(opponent: str, me: str) -> int:
    total = 0
    normalized_me = rps_map[me]
    total += points_map[normalized_me]
    diff = ord(normalized_me) - ord(opponent)
    if diff == 0:
        total += 3
    elif diff == 1 or diff == -2:
        total += 6

    return total


def rock_paper_scissors_2(opponent: str, outcome: str) -> int:
    total = 0
    normalized_outcome = rps_map[outcome]
    total += outcome_map[normalized_outcome]

    if normalized_outcome == "A":
        my_play = loses[opponent]
        total += points_map[my_play]
    elif normalized_outcome == "B":
        total += points_map[opponent]
    else:
        my_play = wins[opponent]
        total += points_map[my_play]
    return total


def part01_answer() -> str:
    total = 0
    rock_paper_scissors_list = load_and_parse()
    for opponent, me in rock_paper_scissors_list:
        total += rock_paper_scissors(opponent, me)
    return str(total)


def part02_answer() -> str:
    total = 0
    rock_paper_scissors_list = load_and_parse()
    for opponent, outcome in rock_paper_scissors_list:
        total += rock_paper_scissors_2(opponent, outcome)
    return str(total)
