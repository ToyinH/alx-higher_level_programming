#!/usr/bin/python3
"""A function that writes a string to a text file(UTF8) and
returns the number of characters written"""


def write_file(filename="", text=""):
    """function that writes a string (text) to a file (filename)
    and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as fr:
        return fr.write(text)
