#!/usr/bin/python3
"""Here is the first class Base. This class will be the base
of all other classes. The goal of it is to manage the id attribute
in all future classes and to avoid duplicating the same code by extension,
same bug.
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string
        representation of list_dictionaries
        
        Args:
            list_dictionaries(list): list of dictionaries
            
        Returns: returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
        
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes the JSON string representation of
        list_objs to a file

        Args:
            list_objs(list of instances): list of instances who inherits
            of Base example list of Rectangle or list of Square instances
        """
        if list_objs is None:
            list_objs = []
        else:
            filename = cls.__name__ + ".json"
            with open(filename, "w", encoding="utf") as file:
                json_str = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )   
                file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns the list of the JSON string
        representaton json_string
        
        Args:
            json_string(string): a string representating a list of
            dictionaries
        
        Returns:
            if json_string is none or empty, return empty list
            otherwise return the list represented by json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
        
    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns an instance with all attributes
        already set

        Args:
            **dictionary: thought as a double pointer to a dictionary
        """
        dummy_instance = cls(1, 2)
        dummy_instance.update(**dictionary)
        return dummy_instance

