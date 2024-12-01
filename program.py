# ruff: noqa: I001

from src.common.dataload import Answers
import src.aoc2024.day01

for answers in Answers.__subclasses__():
    day = answers.__module__.split(".")[-1]
    instance = answers()
    print(f"Advent of Code 2024: {day}-1")
    print(instance.part1())
    print(f"Advent of Code 2024: {day}-2")
    print(instance.part2())
