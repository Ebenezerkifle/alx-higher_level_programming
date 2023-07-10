#!/usr/bin/python3
# 10-square.py
# Abeniezer Kifle
"""Full Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A Square class that inherits a Rectangle class"""

    def __init__(self, size):
        """Intialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        super().integer_validator('Size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """the function to return the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        """returning a string format of a square class"""
        string = "[" + str(self.__class__.name) + "]"
        string += str(self.__size) + "/" + str(self.__size)
        return string
