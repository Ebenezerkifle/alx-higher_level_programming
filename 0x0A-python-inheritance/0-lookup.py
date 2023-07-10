#!/usr/bin/python3
# 0-lookup.py
# Abeniezer Kifle
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Returns a list of availabl attributes of an object"""
    return (dir(obj))
