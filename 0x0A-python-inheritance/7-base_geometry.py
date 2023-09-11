#!/usr/bin/python3
"""An empty class BaseGeometry"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """finding the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
