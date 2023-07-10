#!/usr/bin/python3
# 2--is_same_class.py
# Abeniezer Kifle
"""Defines an object attribute lookup function."""


def is_same_class(obj, a_class):
    """A function checks is an object is an instance of a class
    
    Args:
      obj: an object which would be checked if it is an instance of a class
      a_class: a class

    Return:
        True: if the object is an instance of a class.
        False: if the object is not an instance of a class.
    """
    return type(obj) == a_class
