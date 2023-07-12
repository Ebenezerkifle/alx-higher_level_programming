#!/usr/bin/python3
# 3-to_json_string.py
# Abeniezer Kifle
"""Defins a function that returns the JSON representaion of an object"""
import json


def to_json_string(my_obj):
    """A function that converts an object to a JSON representation

       Args:
          my_obj: an input object to be converted to JSON representation.
       Return: returns a JSON representation of an object.
    """
    return json.dumps(my_obj)
