#!/usr/bin/python3
# 4-inherits_from.py
# Abeniezer Kifle
"""Only Sub class of"""


def inherits_from(obj, a_class):
    """a function to check if the object is an instance of a class that is inherited
       from a specified class

       Args:
         obj: an object
         a_class: a class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
