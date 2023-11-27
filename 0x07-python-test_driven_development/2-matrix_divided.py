#!/usr/bin/python3
"""Defines a function that divides all ints and floats in a matrix"""

def matrix_divided(matrix, div):

    """Function divides all elements in matrix with div
    
    args:
        matrix (list of list): matrix containing elements to be divided
        div (int or float): divisor

    Raise:
        TypeError: if matrix is not a list
        TypeError: if matrix an empty list
        TypeError: if matrix contains a non-list
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(x, list) for x in matrix) or
        not all(isinstance(elem, (int, float)) for elem
        in [x for temp in matrix for x in temp])):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row1 = len(matrix[0])
    for row in matrix:
        if row1 != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
