#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    length = len(my_string)
    for idx in range(length):
        if my_string[idx] not in ('c', 'C'):
            new_string += my_string[idx]
    return new_string
