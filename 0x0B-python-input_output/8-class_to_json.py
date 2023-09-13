#!/usr/bin/python3
"""
A function that returns the dictionary description with simple data structure
(ist, dictionary, string, integer and boolean) for json serialization of an
object.
Do not import any module
"""


def class_to_json(obj):
    """The function that return the dictionary description of obj. All
    attributes of the obj Class are serializable."""
    json_dict = {}
    attributes = dir(obj)
    for attribute_name in attributes:
        if attribute_name.startswith("_"):
            continue
        attribute_value = getattr(obj, attribute_name)
        if isinstance(attribute_value, (list, dict, str, int, bool)):
            json_dict[attribute_name] = attribute_value
    return json_dict
