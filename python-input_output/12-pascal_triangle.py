#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = pascal[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
        pascal.append(row)
    return pascal
