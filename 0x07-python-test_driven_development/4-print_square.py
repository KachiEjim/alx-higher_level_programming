#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """definition of a function that prints a square with the character #
    
    args:
        size (int): size of the square.

    Raise:
        TypeError: if Size is not an integer
        ValueError: if size is less than zero.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    [print('#' * size,) for i in range(size)]
