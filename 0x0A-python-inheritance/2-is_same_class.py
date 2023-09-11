#!/usr/bin/python3
"""A function that returns True if the object is exactly an instance
of the specified class otherwise False"""


def is_same_class(obj, a_class):
    """method that checks if obj is EXACTLY an instance of a_class
    Use type() for exact instance and isinstance() for just an instance"""
    if type(obj) is a_class:
        return True
    else:
        return False
