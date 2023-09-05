#!/usr/bin/python3
"""This module creates a class that defines a Rectangle"""


class Rectangle:
    """A class Rectangle is created here"""
    def __init__(self, width=0, height=0):
        """this is the constructor method."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    def __str__(self):
        """print the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        print_rect = ""
        for _ in range(self.__height):
            print_rect += ("#" * self.__width + "\n")
        return print_rect[:-1]

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {}).format(self.__width, self.__height)"

    @property
    def width(self):
        """This is the getter method."""
        return self.__width

    @width.setter
    def width(self, value):
        """This is the setter method which also checks for errors"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is the getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is the setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method that returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
