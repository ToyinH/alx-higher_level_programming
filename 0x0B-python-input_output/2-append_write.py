#!/usr/bin/python3
"""A function that appends a string at the end of a text file(UTF-8)
and returns the number of character added."""


def append_write(filename="", text=""):
    """A function that appends a string (text) at the end of a
    text file(filename) and returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
