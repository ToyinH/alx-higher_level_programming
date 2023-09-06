#!/usr/bin/python3
"""writing a class with no class or object attribute
that prevents the user from dynamically creating new instance attributes
except if the new instance attribute is called first_name
"""


class LockedClass:
    """LockedClass that prevent instance except first_name"""
    __slots__ = ('first_name',)
