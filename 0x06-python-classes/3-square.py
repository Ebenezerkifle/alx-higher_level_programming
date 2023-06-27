#!/usr/bin/python3
# 0-square.py
# Abeniezer Kifle
"""Define a class Square."""

class Square:
    """A Square is a rectangle that have
    an equale length of the height and width"""
    def __init__(self, size=0):    
           if not isinstance(size, int):
               raise TypeError('size must be an integer')
           elif size < 0:
                raise ValueError('size must be >= 0')
           self.__size = size

    def area(self):
         return self.__size * self.__size
