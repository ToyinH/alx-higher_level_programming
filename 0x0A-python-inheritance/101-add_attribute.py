#!/usr/bin/python3
"""a function that adds a new attribute to an object if possible"""


def add_attribute(obj, name, value):
    """method to add an attribute to an object"""
    if hasattr(obj, '__dict__') or \
            (hasattr(obj, '__slots__') and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
