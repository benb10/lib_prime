"""Tests of lib_prime functions, including unit tests and property based tests.

Contracts are defined on functions in lib_prime, so the property based tests simply
check that the functions don't crash.
"""
from hypothesis import given
from hypothesis.strategies import integers

from lib.lib_prime import get_primes, is_prime, get_pf


def test_get_primes():
    """Check that the correct result is obtained in several cases."""
    assert get_primes(1) == []
    assert get_primes(10) == [2, 3, 5, 7]
    assert get_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                               43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


@given(integers(min_value=1, max_value=10_000))  # max_value of 10_000 to keep tests running quickly
def test_get_primes_does_not_crash(n):
    """Check that the function runs successfully."""
    get_primes(n)


def test_get_primes_vs_is_prime(limit=1_000):
    """Test that the functions get_primes and is_prime agree up to limit."""
    # Use set for faster lookup:
    primes_set = set(get_primes(limit))

    for i in range(1, limit + 1):
        if is_prime(i):
            assert i in primes_set
        else:
            assert i not in primes_set


def test_is_prime():
    """Check that the correct result is obtained in several cases."""
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert not is_prime(6)
    assert is_prime(7)

    assert is_prime(999_983)
    assert is_prime(100_000_000_003)
    assert not is_prime(100_000_000_004)
    assert not is_prime(184*2774)


@given(integers(min_value=1, max_value=1_000_000_000))
def test_is_prime_does_not_crash(n):
    """Check that the function runs successfully."""
    is_prime(n)


def test_get_pf():
    """Check that the correct result is obtained in several cases."""
    assert get_pf(1) == []
    assert get_pf(2) == [2]
    assert get_pf(360) == [2, 2, 2, 3, 3, 5]
    assert get_pf(97) == [97]
    assert get_pf(1024) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    assert get_pf(99) == [3, 3, 11]
    assert get_pf(510510) == [2, 3, 5, 7, 11, 13, 17]


@given(integers(min_value=1, max_value=1_000))  # max_value of 1_000 to keep tests running quickly
def tests_get_pf_does_not_crash(n):
    """Check that the function runs successfully."""
    get_pf(n)
