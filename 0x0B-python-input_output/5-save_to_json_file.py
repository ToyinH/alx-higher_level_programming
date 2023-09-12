#!/usr/bin/python3
"""A function that writes an Object to a text file, using a JSON
representation"""
import json


def save_to_json_file(my_obj, filename):
    """save an object file (my_obj) to filename which is a
    json file. Use dump with s since it is not a string"""
    with open(filename, "w", encoding="utf=8") as file:
        json.dump(my_obj)
