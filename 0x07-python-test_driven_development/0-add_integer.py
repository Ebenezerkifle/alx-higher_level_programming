#!/usr/bin/python3
#0-add_integer.py

"""A function to add two integers a and b"""


def add_integer(a, b=98):
    """Return the sum of two integers a and b
    
    Float argumets are typcasted to integer before addition is performed

    Raises:
        TypeError: If either of the arguments are non-integer or non-float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
