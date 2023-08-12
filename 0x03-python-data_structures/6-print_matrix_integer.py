#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # check if empty and print empty
    if matrix == [[]]:
        print()
    else:
        matrix_len = len(matrix)
        for i in range(matrix_len):
            # inner list lenght is x
            x = len(matrix[i])
            for j in range(x):
                # each element is y
                y = matrix[i][j]
                print("{:d}".format(y), end=" " if j < x - 1 else "\n")
