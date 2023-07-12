#!/usr/bin/python3
#6-load_from_json_file.py
# Abeniezer Kifle
"""Defins a function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """A function to create an object from a json file

       Args:
          filename: a name of a json file.
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        json_string = myFile.read()
        return json.loads(json_string)
