import pytest

from src.aoc2023.day09 import derivative, derivative_all, next_in_sequence, parse, previous_in_sequence

sample_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()


def test_derivative():
    numbers = [0, 3, 6, 9, 12, 15]
    nprime = derivative(numbers)
    assert nprime == [3, 3, 3, 3, 3]


def test_derivative_many():
    num_lines = parse(sample_data)
    actual = derivative_all(numbers=num_lines[0])
    assert actual == [[0, 3, 6, 9, 12, 15], [3, 3, 3, 3, 3], [0, 0, 0, 0]]


@pytest.mark.parametrize("i, expected", [(0, 18), (1, 28), (2, 68)])
def test_next_in_sequence(i: int, expected: int):
    num_lines = parse(sample_data)
    derivatives = derivative_all(numbers=num_lines[i])
    derivateves_next = next_in_sequence(derivatives)
    assert derivateves_next[0][-1] == expected


def test_prev_in_sequence():
    derivatives = derivative_all([10, 13, 16, 21, 30, 45])
    derivatives_prev = previous_in_sequence(derivatives)
    assert derivatives_prev[0][0] == 5
