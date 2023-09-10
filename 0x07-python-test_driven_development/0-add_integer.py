#!/usr/bin/python3
"""
Module to add two integers.
The float is typecasted to an integer before the addition
"""


def add_integer(a, b=98):
    """function that returns the sum of two integers"""
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
