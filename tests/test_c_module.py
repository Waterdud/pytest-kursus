import pytest
from src.c_module import BankAccount, fibonacci, prime_factors, moving_average, normalize_scores

# C-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_fibonacci_small():
    """Test Fibonacci arvude arvutamist."""
    assert [fibonacci(i) for i in range(6)] == [0,1,1,2,3,5]
    assert fibonacci(10) == 55

def test_prime_factors_basic():
    """Test algtegurite leidmist."""
    assert prime_factors(12) == [2,2,3]
    assert prime_factors(97) == [97]

import pytest
from src.c_module import (
    BankAccount,
    fibonacci,
    prime_factors,
    moving_average,
    normalize_scores,
)

def test_prime_factors_basic():
    """Test algtegurite leidmist."""
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(97) == [97]

def test_prime_factors_invalid():
    with pytest.raises(ValueError):
        prime_factors(1)
    with pytest.raises(ValueError):
        prime_factors(0)
    with pytest.raises(ValueError):
        prime_factors(-10)

def test_moving_average_basic():
    values = [1, 2, 3, 4, 5]
    assert moving_average(values, 1) == [1.0, 2.0, 3.0, 4.0, 5.0]
    assert moving_average(values, 2) == [1.5, 2.5, 3.5, 4.5]
    assert moving_average(values, 5) == [3.0]
    assert moving_average(values, 6) == []

def test_moving_average_window_invalid():
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], 0)
    with pytest.raises(ValueError):
        moving_average([1, 2, 3], -1)

def test_normalize_scores_basic():
    assert normalize_scores([0, 50, 100]) == [0.0, 0.5, 1.0]
    assert normalize_scores([25, 75]) == [0.25, 0.75]

def test_normalize_scores_invalid():
    with pytest.raises(ValueError):
        normalize_scores([-1, 50])
    with pytest.raises(ValueError):
        normalize_scores([101])

def test_bankaccount_basic_operations():
    a = BankAccount("Alice", 100)
    assert a.balance() == 100
    a.deposit(50)
    assert a.balance() == 150
    a.withdraw(30)
    assert a.balance() == 120

def test_bankaccount_invalid_init_and_operations():
    with pytest.raises(ValueError):
        BankAccount("", 0)
    with pytest.raises(ValueError):
        BankAccount(123, 0)
    with pytest.raises(ValueError):
        BankAccount("Bob", -10)

    a = BankAccount("A", 100)
    with pytest.raises(ValueError):
        a.deposit(0)
    with pytest.raises(ValueError):
        a.deposit(-10)
    with pytest.raises(ValueError):
        a.withdraw(0)
    with pytest.raises(ValueError):
        a.withdraw(-5)
    with pytest.raises(ValueError):
        a.withdraw(1000)  # more than balance

def test_transfer_to_and_invalid_transfers():
    a = BankAccount("A", 200)
    b = BankAccount("B", 50)
    a.transfer_to(b, 70)
    assert a.balance() == 130
    assert b.balance() == 120

    with pytest.raises(ValueError):
        a.transfer_to("not_account", 10)
    with pytest.raises(ValueError):
        a.transfer_to(b, 0)
    with pytest.raises(ValueError):
        a.transfer_to(b, -1)
    with pytest.raises(ValueError):
        a.transfer_to(b, 10000)


# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
