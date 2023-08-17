#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squareMatrix = []
    for row in matrix:
        squaredRow = [x ** 2 for x in row]
        squareMatrix.append(squaredRow)
    return squareMatrix
