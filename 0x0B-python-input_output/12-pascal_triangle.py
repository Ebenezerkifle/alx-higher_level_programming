#!/usr/bin/python3
#12-pascal_triangle.py
# Abeniezer Kifle
"""Defining a function creating pascal triangle"""


def pascal_triangle(n):
    """Pascal traingle creating function
       Args:
         n: the length of a tree
       Retrun: returns a list of lists of integers
          if an empty list if n less than or equals to 0
    """
    if n <= 0:
        return []
    list_1 = [1]

    if n == 1:
        return [list_1]
    
    list_2 = [1, 1]
    if n == 2: 
        return [list_1, list_2]
    
    triangle = [list_1, list_2]
    for i in range(2, n):
        temp_list = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j] + triangle[i-1][j-1])
        triangle.append(temp_list)
    return triangle
