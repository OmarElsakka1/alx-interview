#!/usr/bin/python3
""" Minimum operations
"""


def minOperations(n):
    """Getting the minimum number of operations

    Args:
        n (int): Number of desired H characters.

    Returns:
        int: Number of minimal operations needed to get n H characters.
    """
    if not isinstance(n, int):
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            done += clipboard
            ops_count += 1
    return ops_count
