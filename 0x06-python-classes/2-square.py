#!/usr/bin/python3
# 0-square.py
# Abeniezer Kifle
"""Define a class Square."""

class Square:
    """A Square is a rectangle that have
    an equale length of the height and width"""
    def __init__(self, size):
           if type(size) is int:
                self.__size = size
           if type(size) is not int:
               raise TypeError('size must be an integer')
           elif size < 0:
                raise ValueError('size must be >= 0')
