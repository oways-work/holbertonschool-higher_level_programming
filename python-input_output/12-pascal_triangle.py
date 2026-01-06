#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns:
        list: A list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    tri = [[1]]
    for i in range(1, n):
        row = [1]
        prev = tri[i - 1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        tri.append(row)
    return tri
