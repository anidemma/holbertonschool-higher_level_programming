#!/usr/bin/python3
"""0-add_integer.py and tests/0-add_integer.txt"""


def add_integer(a, b=98):
    """adds an integer"""
    if isinstance(a, (int, float)) is False:
        raise TypeError('a must be an integer')
    if isinstance(b, (int, float)) is False:
        raise TypeError('b must be an integer')
    return int(a + b)
