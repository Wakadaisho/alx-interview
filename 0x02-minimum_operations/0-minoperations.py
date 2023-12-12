#!/usr/bin/python3
"""
Module to calculate the fewest number of operations
needed to result in exactly n H characters in the file
using two operations on a file starting with 1 H
"""


def minOperations(n) -> int:
    """Calculate the fewest number of operations
    needed to result in exactly n H characters in the file
    using two operations on a file starting with 1 H
    """
    from math import log, floor, sqrt

    if (n <= 1):
        return 0

    # Find first divisor
    divisor: int = n
    max: int = floor(sqrt(n)) + 1

    for i in range(2, max):
        if n % i == 0:
            divisor = i
            break
    if divisor == n:
        return n

    return floor(log(n, divisor) * divisor)
