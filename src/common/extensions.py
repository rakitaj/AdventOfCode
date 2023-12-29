from typing import Collection, Sequence


def single[T](iterable: Collection[T]) -> T:
    if len(iterable) != 1:
        raise ValueError(f"Collection must have a size of exactly 1. Collection is {iterable}")
    else:
        return iterable.__iter__().__next__()


def flatten[T](array: Sequence[T]) -> list[T]:
    result: list[T] = []
    for e in array:
        if isinstance(e, list):
            local_result = flatten(e)
            result.extend(local_result)
        else:
            result.append(e)
    return result


def must[T](value: T | None) -> T:
    """Check that a value must exist. Another way of saying that is the value must not be null."""
    if value is None:
        raise ValueError("Called not_null on a value which is None.")
    return value
