#!/usr/bin/python3
# 102-square.py
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

    @property
    def size(self):
         return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
               raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    
    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
