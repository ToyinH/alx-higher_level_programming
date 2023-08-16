#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # new_matrix = [rwo for row in matrix]
    # now handle the row using value ** 2 for value in row
    new_matrix = [[value ** 2 for value in row] for row in matrix]
    return new_matrix
