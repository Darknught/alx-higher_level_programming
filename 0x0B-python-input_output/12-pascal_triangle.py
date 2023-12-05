#!/usr/bin/python3
"""Module defines a function pascal triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing the pascal
    triangle of n
    Return:
        empty in n <= 0
        n will always be an integer
    """
    if n <= 0:
        return[]
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j -1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
