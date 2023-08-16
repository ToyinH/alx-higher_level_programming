#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        max = 0
        for key in a_dictionary:
            if a_dictionary[key] > max:
                max = a_dictionary[key]
        for key in a_dictionary:
            if a_dictionary[key] == max:
                return key
