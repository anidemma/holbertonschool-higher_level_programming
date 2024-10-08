#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        return ("" + (
            self.__width * str(self.print_symbol) + '\n'
            ) * self.__height).rstrip('\n')

    def __repr__(self) -> str:
        x = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return x

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
