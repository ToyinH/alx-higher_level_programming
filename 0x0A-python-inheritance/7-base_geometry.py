#!/usr/bin/python3
"""A class BaseGeometry."""


class BaseGeometry:
    """an empty class.
    Class which validates value."""
    def area(self):
        """finding the area.
        Raise exception for the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value
        Args:
            name (str): The name of the parameter
            value (int): The parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0"""
        if type(name) is not str:
            raise TypeError
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
