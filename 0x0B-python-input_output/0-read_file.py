#!/usr/bin/python3
# 0-read_file.py
# Abeniezer Kifle
"""Defins a function that reads a given file."""


def read_file(filename=""):
    """A function to read a text file from a file 
       Args:
         filename: the name of file to be read.
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        print(myFile.read())
