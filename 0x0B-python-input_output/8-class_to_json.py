#!/usr/bin/python3
#8-class_to_json.py
# Abeniezer Kifle
"""Returns the dictionary description for JSON serialization"""


def class_to_json(obj):
    """A function to convert an object to JSON srialization
       Args: 
         obj: an object as an input
       Returns: the directory description for JSON serialization.
    """
    return obj.__dict__()
