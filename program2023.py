import src.aoc2023.day01
import src.aoc2023.day02
import src.aoc2023.day03
import src.aoc2023.day04
import src.aoc2023.day05
import src.aoc2023.day06
import src.aoc2023.day07
import src.aoc2023.day08
import src.aoc2023.day09
from src.common.dataload import Answers

for answers in Answers.__subclasses__():
    day = answers.__module__.split(".")[-1]
    instance = answers()
    print(f"Advent of Code 2023: {day}-1")
    print(instance.part1())
    print(f"Advent of Code 2023: {day}-2")
    print(instance.part2())
