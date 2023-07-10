#!/usr/bin/python3
# 1-my_list.py
# Abeniezer Kifle
"""Defines an object attribute lookup function."""

class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """prints sorted elements"""
        print(sorted(self))
