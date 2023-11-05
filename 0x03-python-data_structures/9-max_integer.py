#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        b = my_list[0]
        for item in my_list:
            if item > b:
                b = item
        return (b)
    return (None)
