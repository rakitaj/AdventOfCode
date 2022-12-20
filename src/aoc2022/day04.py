from src.common.dataload import DataLoader


def load_and_parse() -> list[tuple[int, int, int, int]]:
    loader = DataLoader(2022, "day04.txt")
    data = loader.readlines_str()
    result: list[tuple[int, int, int, int]] = list()
    for datum in data:
        pair_one, pair_two = datum.split(",")
        start_one, end_one = pair_one.split("-")
        start_two, end_two = pair_two.split("-")
        item = (int(start_one), int(end_one), int(start_two), int(end_two))
        result.append(item)
    return result


def part01_answer() -> str:
    total = 0
    backpacks = load_and_parse()
    for backpack in backpacks:
        priority_num = priority_of_backpack(backpack)
        total += priority_num
    return str(total)
