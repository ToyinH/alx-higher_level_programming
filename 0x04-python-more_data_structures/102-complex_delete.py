#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    save= []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            save.append(key)
    for item in save:
        del a_dictionary[item]
    return a_dictionary
