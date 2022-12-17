from src.common.dataload import DataLoader


def max_sum_of_lists(numbers_matrix: list[list[int]]) -> int:
    highest = 0
    for line in numbers_matrix:
        s = sum(line)
        if s > highest:
            highest = s
    return highest


def load_and_parse() -> list[list[int]]:
    loader = DataLoader(2022, "day01-1.txt")
    data = loader.readlines_str()
    result: list[list[int]] = list()
    intermediate: list[int] = list()
    for datum in data:
        if datum.isspace():
            result.append(intermediate)
            intermediate = list()
        else:
            intermediate.append(int(datum))
    return result


def day01_part01_answer() -> str:
    list_of_lists = load_and_parse()
    answer = max_sum_of_lists(list_of_lists)
    return str(answer)


def day01_part02_answer() -> str:
    list_of_lists = load_and_parse()
    sums: list[int] = list()
    for l in list_of_lists:
        s = sum(l)
        sums.append(s)
    sums.sort()
    return str(sum(sums[-3:]))
