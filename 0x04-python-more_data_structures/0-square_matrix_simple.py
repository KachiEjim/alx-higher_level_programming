#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    new = list()
    for item in matrix:
        new.append(list(map(lambda x: x ** 2, item)))
    return new
