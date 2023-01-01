from src.common.dataload import DataLoader


class Instruction:
    def __init__(self) -> None:
        self.cycles = 0

    def run(self, registers: dict[str, int]) -> dict[str, int]:
        self.cycles -= 1
        return registers

    def done(self) -> bool:
        return self.cycles <= 0


class Noop(Instruction):
    def __init__(self) -> None:
        self.cycles = 1

    def run(self, registers: dict[str, int]) -> dict[str, int]:
        Instruction.run(self, registers)
        return registers


class Addx(Instruction):
    def __init__(self, value: int) -> None:
        self.cycles = 2
        self.value = value

    def run(self, registers: dict[str, int]) -> dict[str, int]:
        Instruction.run(self, registers)
        self.cycles -= 1
        if self.cycles == 0:
            registers["X"] += self.value
        return registers


class CPUEmulator:
    def __init__(self) -> None:
        self.clock = 0
        self.registers = {"X": 1}
        self.instructions: list[Instruction] = []

    def tick(self) -> None:
        self.clock += 1
        if 0 < len(self.instructions):
            self.registers = self.instructions[0].run(self.registers)
            if self.instructions[0].done():
                self.instructions.pop(0)


def parse_data(lines: list[str]) -> list[Instruction]:
    result: list[Instruction] = list()
    for line in lines:
        parts = line.split()
        if len(parts) == 1:
            result.append(Noop())
        else:
            op, num = parts
            result.append(Addx(int(num)))
    return result


def part01_answer() -> str:
    sum_signal_strength = 0
    loader = DataLoader(2022, "day10.txt")
    data = loader.readlines_str()
    instructions = parse_data(data)
    cpu = CPUEmulator()
    cpu.instructions = instructions
    for i in range(1, 221):
        cpu.tick()
        if (i + 20) % 40 == 0:
            signal_strength = i * cpu.registers["X"]
            sum_signal_strength += signal_strength
    return str(sum_signal_strength)
