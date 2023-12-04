#!/usr/bin/python3
"""Checks for class parent classes"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (object): The object to be checked.
        a_class (type): The specified class to check inheritance against.

    Returns:
        bool: True if obj is an instance of a
        subclass of a_class; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
