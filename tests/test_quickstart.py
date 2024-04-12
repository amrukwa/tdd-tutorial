import numpy as np
import pytest

from scripts import quickstart


def test_foo_increments():
    assert quickstart.foo(3) == 4


def test_show_failure():
    assert False


@pytest.mark.skip(reason="the test is not important at this point")
def test_show_skip():
    assert quickstart.foo(1) == 2


def test_find_letters_has_correct_shape():
    assert len(quickstart.find_letters("hello", "l")) == 2
    assert len(quickstart.find_letters("hello", "x")) == 0


def test_find_letters_gets_indices():
    assert quickstart.find_letters("hello", "l") == [2, 3]
    assert quickstart.find_letters("hello", "o") == [4]
    assert quickstart.find_letters("hello", "a") == []
    assert quickstart.find_letters("hello", "H") == []


def test_find_letters_raises_errors():
    with pytest.raises(ValueError):
        quickstart.find_letters(1, "a")
    with pytest.raises(ValueError):
        quickstart.find_letters("hello", 1)


def test_find_letters_raises_error_with_message():
    with pytest.raises(ValueError) as errorinfo:
        quickstart.find_letters(["a", "x"], 1)
        assert "letter must be a string" in str(errorinfo.value)


def test_get_pi_is_accurate():
    np.testing.assert_almost_equal(quickstart.get_pi(), np.pi, decimal=2)
