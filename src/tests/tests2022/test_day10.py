import pytest
from src.aoc2022.day10 import parse_data, NoOp, AddX, CPUEmulator

data = """noop
addx 3
addx -5""".splitlines()

big_data = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines()


def test_tiny_data():
    instructions = parse_data(data)
    assert len(instructions) == 3
    assert type(instructions[0]) is NoOp
    assert type(instructions[1]) is AddX and instructions[1].value == 3
    assert type(instructions[2]) is AddX and instructions[2].value == -5


def test_tiny_data_5_ticks():
    instructions = parse_data(data)
    cpu = CPUEmulator(instructions)
    assert len(cpu.instructions) == 3
    cpu.tick()
    assert cpu.registers["X"] == 1
    assert len(cpu.instructions) == 2
    cpu.tick()
    assert cpu.registers["X"] == 1
    cpu.tick()
    assert cpu.registers["X"] == 4
    assert len(cpu.instructions) == 1
    cpu.tick()
    assert len(cpu.instructions) == 1
    cpu.tick()
    assert cpu.registers["X"] == -1
    assert len(cpu.instructions) == 0


@pytest.mark.parametrize(
    "cycle_num, expected", [(20, 420), (60, 1140), (100, 1800), (140, 2940), (180, 2880), (220, 3960)]
)
def test_big_data_220_ticks(cycle_num: int, expected: int):
    instructions = parse_data(big_data)
    cpu = CPUEmulator(instructions)
    _ = cpu.tick_many(cycle_num)
    assert cpu.registers["X"] * cycle_num == expected


def test_big_data_220_ticks_total():
    instructions = parse_data(big_data)
    cpu = CPUEmulator(instructions)
    actual = cpu.tick_many(220)
    assert actual == 13140


def test_part_2_draw_letters():
    crt: list[str] = ["", "", "", "", "", ""]
    instructions = parse_data(big_data)
    cpu = CPUEmulator(instructions)
    for i in range(1, 41):
        cpu.tick()
        rx = cpu.registers["X"]
        line_num = abs(i - 1) // 40
        if i % 40 in {rx - 1, rx, rx + 1}:
            crt[line_num] += "#"
        else:
            crt[line_num] += "."
    expected = "##..##..##..##..##..##..##..##..##..##.."
    assert crt[0] == expected
