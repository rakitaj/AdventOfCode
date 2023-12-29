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
        # distance = i * (time - i)
        distance = (i * time) - (i * i)
        if distance > max_distance:
            wins.append(i)
    return wins


class Day06Answers(Answers):
    def part1(self) -> str:
        race1 = BoatRace(40, 215)
        race2 = BoatRace(70, 1051)
        race3 = BoatRace(98, 2147)
        race4 = BoatRace(79, 1005)
        wins1 = calculate_how_to_win(race1.time, race1.max_distance)
        wins2 = calculate_how_to_win(race2.time, race2.max_distance)
        wins3 = calculate_how_to_win(race3.time, race3.max_distance)
        wins4 = calculate_how_to_win(race4.time, race4.max_distance)
        result = len(wins1) * len(wins2) * len(wins3) * len(wins4)
        return str(result)

    def part2(self) -> str:
        race = BoatRace(40709879, 215105121471005)
        wins = calculate_how_to_win(race.time, race.max_distance)
        return str(len(wins))
