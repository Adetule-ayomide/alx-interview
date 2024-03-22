#!/usr/bin/python3

"""In a text file, there is a single character H.
   Your text editor can execute only two operations in this file: Copy All and Paste.
   Given a number n, write a method that calculates the fewest number of operations
   needed to result in exactly n H characters in the file.

   Prototype: def minOperations(n)
   Returns an integer
   If n is impossible to achieve, return 0
"""


def minOperations(n):
    """A function that returns minimum operation"""
    if n <= 1:
        return 0

    """ Initialize a list to store minimum operations for each number up to n"""
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        """ Initialize min_ops[i] to infinity"""
        min_ops[i] = float('inf')

        """ Check all factors of i and update min_ops[i]"""

        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)
                min_ops[i] = min(min_ops[i], min_ops[i // j] + j)


    return min_ops[n]
