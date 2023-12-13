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
    for i in range(2, n):
        if n % i == 0:
            return i + minOperations(n // i)
    return n > 1 and n or 0
