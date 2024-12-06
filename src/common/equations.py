import math
from typing import Generator


def quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    quadratic_sqrt = math.sqrt(b**2 - (4 * a * c))
    root1 = (-b + quadratic_sqrt) / (2 * a)
    root2 = (-b - quadratic_sqrt) / (2 * a)
    return (root1, root2)


def binary_permutations(i: int) -> list[list[int]]:
    result = list(_binary_permutations(i, []))
    return result


def _binary_permutations(i: int, array: list[int]) -> Generator[list[int]]:
    if i == 0:
        yield array
    else:
        copy_zero = array.copy()
        copy_zero.append(0)
        copy_one = array.copy()
        copy_one.append(1)
        # yield from _binary_permutations(i - 1, copy_zero)
        # yield from _binary_permutations(i - 1, copy_one)
        for r in _binary_permutations(i - 1, copy_zero):
            yield r
        for r in _binary_permutations(i - 1, copy_one):
            yield r
