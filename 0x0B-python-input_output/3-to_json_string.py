#!/usr/bin/python3
"""A function that returns the JSON representation of an
object(string)"""
import json


def to_json_string(my_obj):
    """function that returns the json of my_obj
    Note that my_obj is a string therefore dumps is used
    and not dump"""
    return json.dumps(my_obj)
