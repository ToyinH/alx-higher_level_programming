#!/usr/bin/python3
"""Creating a class Square."""


class Square:

    """This is the class Square."""
    def __init__(self, size=0, position=(0, 0)):
        """this is the constructor method for the class."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """retrieve private instance."""
        return self.__position

    @position.setter
    def position(self, value):
        """Method that set position to new value"""
        if not isinstance(value, int) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """
        Method that prints square using # and position where the square
        will be printed
        """
        for _ in range(self.__position[1]):
            print()

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
