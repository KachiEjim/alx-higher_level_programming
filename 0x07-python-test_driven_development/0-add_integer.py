#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Adds two integers or floats.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of the two numbers after typecasting to integers.

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Example:
        >>> add_integer(3, 5.5)
        8
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
