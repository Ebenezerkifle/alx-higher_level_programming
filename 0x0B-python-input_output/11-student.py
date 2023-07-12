#!/usr/bin/python3
#11-student.py
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

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance"""
        if attrs is not None:
            res = {key: self.__dict__[key] for key in self.__dict__.keys() & attrs}
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """sets an attributes of an object with the values of json"""
        for key in json.keys():
            self.__dict__[key] = json[key]
