#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    y = []
    if n <= 0:
        return y
    y = [[1]]
    for z in range(1, n):
        temp = [1]
        for j in range(len(y[z - 1]) - 1):
            curr = y[z - 1]
            temp.append(y[z - 1][j] + y[z - 1][j + 1])
        temp.append(1)
        y.append(temp)
    return y