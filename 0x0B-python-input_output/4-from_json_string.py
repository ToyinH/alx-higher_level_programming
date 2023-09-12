#!/usr/bin/python3
"""A function that returns an object (Python data structure) represented
by a JSON string."""
import json


def from_json_string(my_str):
    """function that returns an object(s python data structure)
    represented by json. Note that a string here so use loads and not
    load. Mnemonics. DJ- dump Json but Load Python"""
    return json.loads(my_str)
