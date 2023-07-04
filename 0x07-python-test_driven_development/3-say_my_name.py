#!/usr/bin/python3
#3-say_my_name.py
# Abeneizer Kifle

"""A function to take first name and last name 
as an input and prints it in order
"""

def say_my_name(first_name, last_name=""):
    """Say my Name
    
    first_name: mandatory
    last_name: optional
    TypeError: both first name and last name must be an integers
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My Name is {} {}'.format(first_name, last_name), end='\n')
