#!/usr/bin/python3

'''
This module contains the function matrix_divided that divides each element
of a matrix bu a numebr
'''


def matrix_divided(matrix, div):
    '''
    This function divides each element of matrix by div

    Each element has to be an int or a float.

    The result is a new matrix with the quotients rounded to 2DP.
    '''

    if matrix == []:
        raise ValueError("matrix can not be empty")

    divided_matrix = []
    row_len_check = len(matrix[0])
    new_row = []

    for row in matrix:
        if len(row) != row_len_check:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    else:
        if div == 0:
            raise ZeroDivisionError("division by zero")
        else:
            for row in matrix:
                for i in row:
                    if not isinstance(i, (int, float)):
                        raise TypeError("matrix must be a matrix (list of list) of integers/floats")
            for row in matrix:
                new_row = [round(number / div, 2) for number in row]
                divided_matrix.append(new_row)

            return divided_matrix
