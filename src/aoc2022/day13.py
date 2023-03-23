from src.common.extensions import flatten
import json


def compare_lines(line1: str, line2: str) -> bool:
    line1_parsed = json.loads(line1)
    line2_parsed = json.loads(line2)
    left = flatten(line1_parsed)
    right = flatten(line2_parsed)
    for i in range(len(right)):
        if left[i] == right[i] and i == len(right) - 1 and len(right) < len(left):
            return False
        if left[i] > right[i]:
            return False
    return True
