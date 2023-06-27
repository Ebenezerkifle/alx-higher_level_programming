#!/usr/bin/python3
# 101-square.py
# Abeniezer Kifle
"""Define a class Square."""

class Square:
    """A Square is a rectangle that have
    an equale length of the height and width"""
    def __init__(self, size=0, position=(0, 0)):
           if not isinstance(position, tuple):
               raise TypeError('position must be a tuple of 2 positive integers')    
           if not isinstance(size, int):
               raise TypeError('size must be an integer')
           elif size < 0:
                raise ValueError('size must be >= 0')
           self.__size = size
           self.__position = position

    def area(self):
         return (self.__size * self.__size)

    @property
    def size(self):
         return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
               raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
         return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.__size == 0:
             print("")
             return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print("_", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
