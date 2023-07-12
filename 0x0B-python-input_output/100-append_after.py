#!/usr/bin/python3
# 100-append_after.py
# Abeniezer Kifle
"""Defining a function that append a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """A function that appends a line of text after a specific text

       Args:
           filename: (string) the name of a file
           search_string: (string) the string on which a new text appends
           new_string: (string) a string to be appended    
    """
    st = ""
    with open(filename, mode='r', encoding='utf-8') as myFile:
        while True:
            line = myFile.readline()
            if line == "":
                break
            st += line
            if search_string in line:
                st += new_string + "\n"
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(st)
