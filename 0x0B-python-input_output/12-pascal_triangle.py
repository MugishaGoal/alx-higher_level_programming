#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row_data = []
        if i == 0:
            row_data.append(1)
        else:
            prev_row = triangle[i - 1]
            for j in range(i + 1):
                if j == 0 or j == i:
                    row_data.append(1)
                else:
                    value = prev_row[j - 1] + prev_row[j]
                    row_data.append(value)
        triangle.append(row_data)

    return triangle
