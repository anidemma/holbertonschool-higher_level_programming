#!/usr/bin/python3
"""write a string to a text file"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
