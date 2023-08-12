#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_int = 0
    for integer in my_list:
        if integer > max_int:
            max_int = integer
    return max_int
