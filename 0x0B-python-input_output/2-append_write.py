#!/usr/bin/python3
# 2-append_write.py
# Abeniezer Kifle
"""Defins a function that append a text to a given file."""


def append_write(filename="", text=""):
    """A function to append a given string to an existing file

       Args:
          filename: the name of file
          text: a string value to be added to the file
       Returns: the number of characters added'
    """
    with open(filename, mode="a", encoding='utf-8') as myFile:
        myFile.write(text)
    return len(text)
