#!/usr/bin/python3
"""read a text file"""


def read_file(filename=""):
    """read a  text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
