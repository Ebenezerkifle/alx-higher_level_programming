#!/usr/bin/python3
# 1-write_file.py
# Abeniezer Kifle
"""Defins a function that reads a given file."""


def write_file(filename="", text=""):
    """A function that write a string to a text file

       Args:
          filename: the name of the file
          text: the string to be copied to the file
       Retruns:
          a number of characters written
    """
    charLength = 0
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(text)
    with open(filename, encoding='utf-8') as f:
        charLength = len(f.read())
    return charLength
