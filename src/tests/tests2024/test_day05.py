from src.aoc2024.day05 import Day05Parsed, is_page_update_in_order

lines = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()


def test_known_good_line():
    parsed = Day05Parsed(lines)
    is_in_order = is_page_update_in_order(parsed.page_updates[0], parsed.rules)
    assert is_in_order is True
