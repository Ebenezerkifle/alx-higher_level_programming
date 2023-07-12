#!/usr/bin/python3
#5-save_to_json_file.py
# Abeniezer Kifle
"""Defins a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """A function to save an object which is converted to JSON
       representation

       Args: 
          my_obj: an object to be converted to JSON and saved to a file
          filename: a file name
    """
    json_string = json.dumps(my_obj)

    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(json_string)
