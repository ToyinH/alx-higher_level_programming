#!/usr/bin/python3
"""A function that reads a text file (UTF8) and print it to stdout"""


def read_file(filename=""):
    """Function that reads filename and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        f_read = f.read()
        print(f_read, end="")
