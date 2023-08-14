#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    column = 0
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                end = "\n"
            else:
                end = " "
            print("{:d}".format(row[i]), end=end)   
