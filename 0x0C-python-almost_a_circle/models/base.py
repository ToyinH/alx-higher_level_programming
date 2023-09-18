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

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf") as file:
                json_str = file.read()
                dict_list = json.loads(json_str)
                return [cls.create(**obj_dict) for obj_dict in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to file in csv
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", encoding="utf-8") as file:
            if cls.__name__ == "Rectangle":
                file.write("id,width,height,x,y\n")
            elif cls.__name__ == "Square":
                file.write("id,size,x,y\n")

            for obj in list_objs:
                obj_data = [str(getattr(obj, attr)) for attr in obj.__dict__]
                file.write(",".join(obj_data) + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """method that deserializes in csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                if cls.__name__ == "Rectangle":
                    attributes = file.readline().strip().split(",")
                elif cls.__name__ == "Square":
                    attributes = file.readline().strip().split(",")

                instances = []

                for line in file:
                    data = line.strip().split(",")
                    obj_data = {attr: int(value) for attr, value in zip(
                        attributes, data
                        )}
                    instances.append(cls.create(**obj_data))

                return instances
        except FileNotFoundError:
            return []
