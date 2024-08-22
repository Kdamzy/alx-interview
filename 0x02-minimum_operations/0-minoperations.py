#!/usr/bin/python3
""" 0-minoperations"""


def minOperations(n):
    """ minOperations """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # evenly divide the total by root = total operations
            ops += root
            # set n to remainder
            n = n / root
            # reduce root to find remainder smaller value that will evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops
