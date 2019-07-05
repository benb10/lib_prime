"""Reusable library functions related to prime numbers."""
from time import time
from collections import defaultdict
from dpcontracts import require, ensure


@require("`limit` must be an integer > 0", lambda args: isinstance(args.limit, int) and args.limit > 0)
@ensure("the result must be a list", lambda args, result: isinstance(result, list))
@ensure("all elements of list must be integers", lambda args, result: all(isinstance(i, int) for i in result))
@ensure("the list must be sorted", lambda args, result: result == sorted(result))
def get_primes(limit):
    """Return sorted list of all primes <= limit.

    23-06-2019 tested an alternative of this using is_prime function.  This function was much faster.
    """
    print(f'\nCalculating primes up to {limit}... ', end='')
    start_time = time()
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True

    for i in primes:
        i_multiples = range(2*i, limitn, i)
        for f in i_multiples:
            primes[f] = False
    print(f'Finsished. Took {time() - start_time} seconds.\n')
    return sorted([i for i in primes if primes[i] is True])  # Or change to set


@require("`n` must be an integer > 0", lambda args: isinstance(args.n, int) and args.n > 0)
@ensure("the result must be a boolean", lambda args, result: isinstance(result, bool))
def is_prime(n):
    """Return True if n is prime.

    Copied from https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-
    if-a-number-is-prime
    """
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    test_int = 5
    increment = 2

    # test_int iterates through odd numbers, also skipping multiples of 3
    # () means number is skipped
    # test_int = 5, 7, (9), 11, 13, (15), 17, 19, (21), 23

    while test_int * test_int <= n:
        if n % test_int == 0:
            return False
        test_int += increment
        increment = 6 - increment

    return True


def product(list):
    """Return the product of all elements in input list.

    Helper function.
    """
    p = 1
    for i in list:
        p *= i
    return p


@require("`n` must be an integer > 0", lambda args: isinstance(args.n, int) and args.n > 0)
@ensure("the result must be a list", lambda args, result: isinstance(result, list))
# these 2 ensures are covered by the one below:
# @ensure("all elements of list must be integers", lambda args, result: all(isinstance(i, int) for i in result))
# @ensure("all elements of list are > 1", lambda args, result: all(i > 1 for i in result))
@ensure("all elements of list must be prime", lambda args, result: all(is_prime(i) for i in result))
@ensure("the list must be sorted", lambda args, result: result == sorted(result))
@ensure("list elements must multiply to give n", lambda args, result: product(result) == args.n)
def get_pf(n):
    """Return ascending list of the prime factors of a number, without needing input primes list."""
    if n == 1:
        return []
    pf = []
    limitn = n + 1
    primes = defaultdict(lambda: True)

    for i in range(2, limitn):
        if n == 1:
            break
        i_multiples = range(2*i, limitn, i)
        for f in i_multiples:
            primes[f] = False
        if primes[i]:
            # At this point we can be sure that i is prime
            while n % i == 0:
                n = n//i
                pf.append(i)
    return pf
