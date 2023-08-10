#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        letter = str[i]
        letter_ascii = ord(letter)
        if letter_ascii >= 97 and letter_ascii <= 122:
            letter_ascii -= 32
        cap_letter = chr(letter_ascii)
        print("{}".format(cap_letter), end="")
    print("")
