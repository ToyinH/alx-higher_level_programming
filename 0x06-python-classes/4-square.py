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

    def area(self):
        """
        Calculat the area of the square.
        Return the gotten area.
        """
        return self.__size ** 2


    @property
    def size(self):

        """Method to retrieve private object attribute, size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Method that set the size with value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
