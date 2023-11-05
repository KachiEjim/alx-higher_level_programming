#!/usr/bin/python3


def no_c(my_string):
    new = "".join(c for c in my_string if c.upper() != 'C')
    return (new)
