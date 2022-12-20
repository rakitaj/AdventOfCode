from typing import TypeVar, Collection

T = TypeVar("T")


def single(iterable: Collection[T]) -> T:
    if len(iterable) != 1:
        raise ValueError(f"Collection must have a size of exactly 1. Collection is {iterable}")
    else:
        return iterable.__iter__().__next__()
