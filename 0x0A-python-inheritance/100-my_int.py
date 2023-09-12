#!/usr/bin/python3
"""A class MyInt which inherits from int and switch the operation
of == and !="""


class MyInt(int):
    """The new class which inherit from int and switch the function of ==
    and !="""
    def __eq__(self, other):
        """the equal method"""
        return super().__ne__(other)

    def __ne__(self, other):
        """the not equal method"""
        return super().__eq__(other)
