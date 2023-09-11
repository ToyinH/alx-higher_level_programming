#!/usr/bin/python3
"""A class BaseGeometry."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instantiation method."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height
