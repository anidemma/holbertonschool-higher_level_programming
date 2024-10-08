#!/usr/bin/python3
"""This module contains the function taht prints square"""


def print_square(size):
    """prints square usign #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size <= 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
