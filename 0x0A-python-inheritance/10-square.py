#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """The Square class which inherits from Rectangle."""
    def __init__(self, size):
        """The instantiation method for Square"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))

    def area(self):
        """The method that finds the area of the square."""
        return self.__size ** 2
