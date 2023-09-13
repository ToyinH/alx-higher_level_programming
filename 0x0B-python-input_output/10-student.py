#!/usr/bin/python3
"""A class Student that defines a student by first_name, last_name
and age. Include a method that retrieves a dictionary representation of a
Student instance sames as 8-class_to_json.py"""


class Student:
    """Creating a class Student that defines a student with first_name
    last_name and age. Also retrieves a dictionary representation of
    a student instance created"""
    def __init__(self, first_name, last_name, age):
        """instantialization method with public attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method that retrieves a dictionary representation of a
        Student instance. If attrs is a list of strings, only
        attributes names contained in the list must be retrieved"""
        if attrs is None:
            json_dict = {
                    "first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        else:
            for attribute_name in attrs:
                if hasattr(self, attribute_name):
                    json_dict[attribute_name] = getattr(self, attribute_name)
        return json_dict
