#!/usr/bin/python3
"""Returns the list of available attributes and methods of an objecs"""


def lookup(obj):
    """Returns a list of obj methods and attributes

    args:
        obj (object): input object

    Return: Returns a list
    """
    return (dir(obj))
