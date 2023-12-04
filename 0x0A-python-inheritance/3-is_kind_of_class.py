#!/usr/bin/python3
"""Checks if an object is of a type"""


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of,
    or if the object is an instance of a
      class that inherited from, the specified class ; otherwise False

        args:
            obj (object): Object to be typr checked
            a_class (type): type to used for the check.

        Return:
            bool: True of object is of type a_class
            otherwise false.

    """
    return (isinstance(obj, a_class))
