#!/usr/bin/python3
"""A class that validates an input"""


class BaseGeometry:
    """A class that is based
    on class BaseGeometry():"""

    def area(self):
        """Public instance method: def area(self): that
        raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method: def integer_validator
        (self, name, value): that validates value:

        args:
            name (str): name passed
            value (int): interger passed

        Raises:
            if value is not an integer: TypeError exception,
            with the message <name> must be an integer
            if value is less or equal to 0: raise a ValueError
            exception with the message <name> must be greater than 0
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
