from src.common.dataload import Answers
import src.aoc2023.day01
import src.aoc2023.day02
import src.aoc2023.day03
import src.aoc2023.day04
import src.aoc2023.day05

for answers in Answers.__subclasses__():
    day = answers.__module__.split(".")[-1]
    instance = answers()
    print(f"Advent of Code 2023: {day}-1")
    print(instance.part1())
    print(f"Advent of Code 2023: {day}-2")
    print(instance.part2())


print("Advent of Code 2023: 4-1")
print(src.aoc2023.day04.part01_answer())
print("Advent of Code 2023: 4-2")
print(src.aoc2023.day04.part02_answer())


print("Advent of Code 2023: 5-1")
print(src.aoc2023.day05.part01_answer())
# print("Advent of Code 2023: 5-2")
# print(src.aoc2023.day05.part02_answer())
