#!/usr/bin/python3
"""Creating a class Square."""


class Square:
    """This is the class Square."""
    def __init__(self, size=0):
        """this is the constructor method for the class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
