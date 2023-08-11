#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for column in range(row):
            if column == row:
                end = "\n"
            else:
                end = " "
            print(matrix[row][column], end=end)
