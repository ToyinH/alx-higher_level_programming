#!/usr/bin/python3
"""A function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    This function returns the attributes and methods in this object.
    The dir() function returns the attributes and methods as a list
    while the vars() function returns it as a dictionary
    """
    return dir(obj)
