#!/usr/bin/python3
"""Here is the first class Base. This class will be the base
of all other classes. The goal of it is to manage the id attribute
in all future classes and to avoid duplicating the same code by extension,
same bug.
"""


class Base:
    """creating the class Base to manage id attribute."""
    __nb_objects = 0
    def __init__(self, id=None):
        """class constructor assigned none to id if not provided"""
        if id is not None:
            self.id = id
        else:
           Base. __nb_objects += 1
           self.id = Base.__nb_objects
