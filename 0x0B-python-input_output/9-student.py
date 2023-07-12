#!/usr/bin/python3
#9-student.py
# Abeniezer Kifle
"""Defining a class called Student"""


class Student:
    """A student class

       Args:
          first_name: (string) first name
          last_name: (string) last name
          age: (int) age
          # which are public instance attributes
    """
    def __init__(self, first_name, last_name, age):
        """Initializes the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns a dictionary representation of a Student instance"""
        return self.__dict__()
