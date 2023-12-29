import math


def quadratic(a: int, b: int, c: int) -> tuple[float, float]:
    quadratic_sqrt = math.sqrt(b**2 - (4 * a * c))
    root1 = (-b + quadratic_sqrt) / (2 * a)
    root2 = (-b - quadratic_sqrt) / (2 * a)
    return (root1, root2)
