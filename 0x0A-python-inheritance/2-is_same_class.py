#!/usr/bin/python3
"""Checks if an object is of a specified class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class.

    Args:
        obj (object): The object to be checked
        a_class (type): Class used for the check.

    Returns:
        bool: True if obj is an instance of a_class; otherwise False.
    """
    return (type(obj) == a_class)
