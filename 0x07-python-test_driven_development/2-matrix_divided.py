#!/usr/bin/python3
#0-add_integer.py
# Abeniezer Kifle
"""A function that divides all elements of a matrix by a comman factor"""


def matrix_divided(matrix, div):
    """
    matrix: a matrix to be divided
    div: an integer to divid each elements of a matrix
    TypeError: matrix must be a list of lists and each elements on it must be either int or float.
    TypeError: The length of each row should be equal
    TypeError: Dividend must be an integer or float
    ZeroDivisionError: Dividend can't be zero
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, int) or isinstance(element, float)
                for element in [num for row in matrix for num in row])):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
