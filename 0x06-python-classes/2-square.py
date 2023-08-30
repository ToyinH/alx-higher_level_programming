#!/usr/bin/python3
"""Creating a class Square."""


class Square:
    """This is the class Square."""
    def __init__(self, size=0):
        """this is the constructor method for the class."""
        try:
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")

