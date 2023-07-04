#!/usr/bin/python3
#0-add_integer.py
# Abeniezer Kifle
"""A function that divides all elements of a matrix"""

def matrix_divided(matrix, div):
    """
    matrix: a matrix to be divided
    div: an integer to divid each elements of a matrix
    """
    

    if(len(matrix) == 0):
        return
    
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[]]
    col_size = len(matrix[0])
    for i in range(len(matrix)):
        if col_size != len(matrix[i]):
            raise TypeError('Each row of the matrix must have the same size')
        row = []
       
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
            row.append(round(matrix[i][j] / div, 2))
            print(len(row))
        new_matrix.append(row)
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)