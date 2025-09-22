import pytest
from src.a_basics import (
    add, sub, mul, div, sum_list, is_even, factorial, reverse_string,
    is_palindrome, to_title_case, clamp, median, unique_letters, safe_int, nth_root
)


def test_add_basic():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_sub_basic():
    assert sub(10, 7) == 3
    assert sub(5, 3) == 2
    assert sub(5, 0) == 5


def test_multiply_basic():
    assert mul(1, 2) == 2
    assert mul(2, 2) == 4
    assert mul(3, 3) == 9


def test_div_basic():
    assert div(2, 2) == 1
    assert div(6, 2) == 3
    assert div(8, 2) == 4


def test_sum_list_basic():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([10, -5, 5]) == 10
    assert sum_list([]) == 0


def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False
    assert is_even(0) is True


def test_factorial():
    assert factorial(0) == 1
    assert factorial(3) == 6
    with pytest.raises(ValueError):
        factorial(-1)


def test_reverse_string():
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"


def test_is_palindrome():
    assert is_palindrome("aba") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("abc") is False


def test_to_title_case():
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("python code") == "Python Code"


def test_clamp():
    assert clamp(5, 1, 10) == 5
    assert clamp(-1, 0, 5) == 0
    assert clamp(100, 0, 50) == 50


def test_median():
    assert median([1, 3, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    with pytest.raises(ValueError):
        median([])


def test_unique_letters():
    assert unique_letters("abcABC") == {"a", "b", "c"}
    assert unique_letters("123!?") == set()
    assert unique_letters("Hello") == {"h", "e", "l", "o"}


def test_safe_int():
    assert safe_int("123") == 123
    assert safe_int("abc", default=0) == 0
    assert safe_int("10") == 10


def test_nth_root():
    assert nth_root(9, 2) == 3
    assert nth_root(27, 3) == 3
    with pytest.raises(ValueError):
        nth_root(-4, 2)
    with pytest.raises(ValueError):
        nth_root(10, 0)
