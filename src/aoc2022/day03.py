from src.common.dataload import DataLoader
from src.common.extensions import single


def load_and_parse() -> list[str]:
    loader = DataLoader(2022, "day03.txt")
    data = loader.readlines_str()
    return data


def priority(character: str) -> int:
    num = ord(character)
    if 65 <= num and num <= 90:
        return num - 38
    else:
        return num - 96


def priority_of_backpack(contents: str) -> int:
    half = len(contents) // 2
    first_half_set = set(contents[:half])
    second_half_set = set(contents[half:])
    common_element = first_half_set.intersection(second_half_set)
    value = priority(single(common_element))
    return value


def part01_answer() -> str:
    total = 0
    backpacks = load_and_parse()
    for backpack in backpacks:
        priority_num = priority_of_backpack(backpack)
        total += priority_num
    return str(total)


def part02_answer() -> str:
    total = 0
    backpacks = load_and_parse()
    i = 0
    while i < len(backpacks):
        first_set = set(backpacks[i].strip())
        second_set = set(backpacks[i + 1].strip())
        third_set = set(backpacks[i + 2].strip())
        common_element = first_set.intersection(second_set).intersection(third_set)
        value = priority(single(common_element))
        total += value
        i += 3
    return str(total)
