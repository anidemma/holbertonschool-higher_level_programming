#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """sort list"""
    def print_sorted(self):
        print(sorted(self))
