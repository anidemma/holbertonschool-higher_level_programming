#!/usr/bin/python3
"""define square"""


class Square:
    """square"""
    __size = None

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self) -> int:
        return self.__size ** 2

     def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            for ii in range(0, self.__size):
                print("#", end="")
            print()
