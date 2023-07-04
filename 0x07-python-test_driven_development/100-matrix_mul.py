#!/usr/bin/python3
# 100-matrix_mul.py
# Abeniezer Kifle
"""A function to multiply two matrixes"""

def matrix_mul(m_a, m_b):
    """
    m_a: matrix one
    m_b: matrix two

    """
    if m_a is [] or m_a is [[]]:
        raise ValueError("m_a can't be empty")
    if m_b is [] or m_b is [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError('m_b must be a list of lists')

    if not all(isinstance(element, int) or isinstance(element, float)
                for element in [num for row in m_a for num in row]):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(element, int) or isinstance(element, float)
                for element in [num for row in m_b for num in row]):
        raise TypeError('m_b should contain only integers or floats')

    if not all(len(m_a[0]) == len(row) for row in m_a):
        raise TypeError('each row of m_a must be of the same size')
    if not all(len(m_b[0]) == len(row) for row in m_b):
        raise TypeError('each row of m_b must be of the same size')

    """case: Two matrixs can't be multiplied
        column of m_a should be equals to row of m_b
    """
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
    
