#!/usr/bin/python3
#4-print_square.py
# Abeneizer Kifle

"""A function that prints a square with a character #"""

def print_square(size):
    """
    size: The size a square
    TypeError: size must be an integer
    ValueError: size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#' , end="")
        print("", end="\n")
