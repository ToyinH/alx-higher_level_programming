#!/usr/bin/python3
"""A function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides a matrix by div and
    returns new matrix with the result"""
    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
 
    for row in matrix:
        num = element in row
        if (not isinstance(num, int) and not isinstance(num, int)):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            "integers/floats")

