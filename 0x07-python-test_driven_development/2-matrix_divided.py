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
    if type(matrix) is not list or type(matrix[0]) is not list or \
            (len(matrix) == 0) or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) \
                of integers/floats")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
    return [[round(num / div, 2) for num in row] for row in matrix]
