#!/usr/bin/python3
# 11-square.py
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
        self.integer_validator('Size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returning a string format of a square class"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
