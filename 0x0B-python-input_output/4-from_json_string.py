#!/usr/bin/python3
# 4-from_json_string.py
# Abeniezer Kifle
"""Defins a function that returns an object for the JSON representaion"""
import json


def from_json_string(my_str):
    """A function that converts a JSON representation to an object

       Args:
          my_str: an input JSON string to be converted to an object.
       Return: returns an object.
    """
    return json.loads(my_str)
