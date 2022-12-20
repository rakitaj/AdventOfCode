from src.common.extensions import single


def test_single():
    set_of_one = {"A"}
    assert single(set_of_one) == "A"
