#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # the condition for the loop comes first in this syntax
    # if x is not search, go for the loop, else dont but insert replace
    new_list = [x if x != search else replace for x in my_list]
    return new_list
