import math
from src.common.equations import quadratic
from src.common.dataload import DataLoader, Answers
from dataclasses import dataclass


@dataclass
class BoatRace:
    time: int
    max_distance: int


def calculate_how_to_win(time: int, max_distance: int) -> list[int]:
    """Return a list of button hold times which win the race."""
    wins: list[int] = list()
    for i in range(time):
        distance = i * (time - i)
        if distance > max_distance:
            wins.append(i)
        else:
            if len(wins) > 0:
                print("Break early")
                break
    return wins


def calculate_how_to_win_math(time: int, max_distance: int) -> int:
    """https://en.wikipedia.org/wiki/Quadratic_formula
    d = i * (t - i)
    d = it - i^2
    0 = -i^2 + it - d
    """
    root1, root2 = quadratic(-1, time, -max_distance)
    wins = math.floor(root2) - (math.ceil(root1) - 1)
    return wins


class Day06Answers(Answers):
    def part1(self) -> str:
        race1 = BoatRace(40, 215)
        race2 = BoatRace(70, 1051)
        race3 = BoatRace(98, 2147)
        race4 = BoatRace(79, 1005)
        wins1 = calculate_how_to_win_math(race1.time, race1.max_distance)
        wins2 = calculate_how_to_win_math(race2.time, race2.max_distance)
        wins3 = calculate_how_to_win_math(race3.time, race3.max_distance)
        wins4 = calculate_how_to_win_math(race4.time, race4.max_distance)
        return str(wins1 * wins2 * wins3 * wins4)

    def part2(self) -> str:
        race = BoatRace(40709879, 215105121471005)
        wins = calculate_how_to_win_math(race.time, race.max_distance)
        return str(wins)
