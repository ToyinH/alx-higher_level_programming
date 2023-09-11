#!/usr/bin/python3
"""A class Mylist that inherits from list.
Included is a method print_sorted that prints the list but sorted
Assume that the list is of type int.
"""


class MyList(list):
    """Here is the subclass which inherit from list."""
    def print_sorted(self):
        """function that print sorted list"""
        print(sorted(self))
