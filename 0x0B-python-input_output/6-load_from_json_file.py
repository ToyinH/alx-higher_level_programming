#!/usr/bin/python3
"""A function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """function that creates an object from a
    json file. USe load without s here since it is not a string"""
    with open(filename, "r", encoding="utf-8") as file:
        json.load(file)
