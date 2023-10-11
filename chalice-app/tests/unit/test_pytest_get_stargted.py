import pytest


def plus_one(x):
    return x + 1


@pytest.mark.learning
def test_four_plus_one_is_5():
    assert plus_one(4) == 5


@pytest.mark.learning
def test_three_plus_one_isnt_5():
    assert plus_one(3) != 5


@pytest.mark.learning
def test_three_plus_one_is_5_will_raises_assertion_error():
    with pytest.raises(AssertionError):
        assert plus_one(3) == 5
