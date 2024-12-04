from src.common.dataload import Answers
from src.aoc2024 import *

for answers in Answers.__subclasses__():
    day = answers.__module__.split(".")[-1]
    instance = answers()
    print(f"Advent of Code 2023: {day}-1")
    print(instance.part1())
    print(f"Advent of Code 2023: {day}-2")
    print(instance.part2())
