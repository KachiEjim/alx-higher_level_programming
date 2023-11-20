#!/usr/bin/python3

from sys import stderr

def safe_function(fct, *args):
    arg = []
    for i in range(len(args)):
        arg.append(args[i])
    try:
        result = fct(arg[0], arg[1])
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return (None)
    return (result)
