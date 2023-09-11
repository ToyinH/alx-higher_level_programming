#!/usr/bin/python3
"""
A function that returns True if an object is directly
or indirectly an instance of a class
"""


def inherits_from(obj, a_class):
    """A function that returns True if obj is an instance
    of a_class either directly or indirectly"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
