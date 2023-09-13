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

    def to_json(self):
        """method that retrieves a dictionary representation of a
        Student instance."""
        json_dict = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        return json_dict
