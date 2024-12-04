from __future__ import annotations

from typing import Sequence

from src.common.dataload import DataLoader


class Instruction:
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        self.cycles = 0

    def visit(self, cpu: CPUEmulator) -> None:
        pass

    def done(self) -> bool:
        return True

    def __repr__(self) -> str:
        return f"{type(self)} cycles:{self.cycles}"


class NoOp(Instruction):
    def __init__(self) -> None:
        super().__init__("noop", 0)

    def visit(self, cpu: CPUEmulator) -> None:
        self.cycles += 1

    def done(self) -> bool:
        return self.cycles == 1

    def __repr__(self) -> str:
        base_repr = super().__repr__()
        return f"{base_repr} - NoOp"


class AddX(Instruction):
    def __init__(self, value: int):
        super().__init__("addx", value)

    def visit(self, cpu: CPUEmulator) -> None:
        self.cycles += 1
        if self.cycles == 2:
            cpu.registers["X"] += self.value

    def done(self) -> bool:
        return self.cycles == 2

    def __repr__(self) -> str:
        base_repr = super().__repr__()
        return f"{base_repr} - AddX {self.value}"


class CPUEmulator:
    def __init__(self, instructions: list[Instruction]) -> None:
        self.registers = {"X": 1}
        self.instructions = instructions

    def tick(self) -> None:
        if 0 < len(self.instructions):
            self.instructions[0].visit(self)
            if self.instructions[0].done():
                self.instructions.pop(0)

    def tick_many(self, num: int) -> int:
        total = 0
        for i in range(1, num + 1):
            if (i + 20) % 40 == 0:
                total += self.registers["X"] * i
            self.tick()
        return total


def parse_data(lines: Sequence[str]) -> list[Instruction]:
    result: list[Instruction] = list()
    for line in lines:
        parts = line.split()
        if len(parts) == 1:
            result.append(NoOp())
        else:
            _op, num = parts
            result.append(AddX(int(num)))
    return result


def part01_answer() -> str:
    loader = DataLoader(2022, "day10.txt")
    data = loader.readlines_str()
    instructions = parse_data(data)
    cpu = CPUEmulator(instructions)
    total = cpu.tick_many(220)
    return str(total)


def part02_answer() -> list[str]:
    crt: list[str] = ["", "", "", "", "", ""]
    loader = DataLoader(2022, "day10.txt")
    data = loader.readlines_str()
    instructions = parse_data(data)
    cpu = CPUEmulator(instructions)
    for i in range(1, 241):
        cpu.tick()
        rx = cpu.registers["X"]
        line_num = abs(i - 1) // 40
        if i % 40 in {rx - 1, rx, rx + 1}:
            crt[line_num] += "#"
        else:
            crt[line_num] += "."
    return crt
