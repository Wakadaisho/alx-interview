#!/usr/bin/python3
"""Function to check number of minimum coins to reach a total
"""

def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.
    """
    if total <= 0:
        return 0
    solutions = [total + 1] * (total + 1)
    solutions[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                solutions[i] = min(solutions[i], 1 + solutions[i - coin])

    return solutions[total] if solutions[total] != total + 1 else -1
