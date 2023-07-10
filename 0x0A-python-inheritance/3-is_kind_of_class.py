#!/usr/bin/python3
# 3-is_kind_of_class.py
# Abeniezer Kifle
"""Write a function that returns True if the object is 
an instance of, or if the object is an instance of a class 
that inherited from, the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """A function checks is an object is an instance of a class
    
    Args:
      obj: an object which would be checked if it is an instance of a class
      a_class: a class

    Return:
        True: if the object is an instance of a class.
        False: if the object is not an instance of a class.
    """

    if isinstance(obj, a_class):
        return True
    return False