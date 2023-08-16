#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0

    prev_val = 0
    total = 0
    roman_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 100
            }
    for letter in reversed(roman_string):
        value = roman_dic.get(letter, 0)
        if value >= prev_val:
            total += value
        else:
            total -= value
    prev_val = value
    return total
