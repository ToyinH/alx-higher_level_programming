#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # create a list to save the keys that you want to delete
    # this is because deleting the keys while iterating a dictionary
    # throws an error because the size is modified.
    # This is peculiar to dictionary and not to list
    # you can modify lists while iterating
    save = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            save.append(key)
    for item in save:
        del a_dictionary[item]
    return a_dictionary
