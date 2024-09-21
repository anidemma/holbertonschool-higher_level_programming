#!/usr/bin/python3
"""define square"""


class Square:
    """square"""
    __size = None

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self) -> int:
        return self.__size ** 2
