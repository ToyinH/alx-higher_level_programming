#!/usr/bin/python3
"""An empty class BaseGeometry"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """finding the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value"""
        if type(name) is not str:
            raise TypeError("not a string")
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
