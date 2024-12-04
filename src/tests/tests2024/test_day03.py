from src.aoc2024.day03 import multiply_line_conditional


def test_do_dont_parsing():
    data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    total = multiply_line_conditional(data)
    assert total == 48
