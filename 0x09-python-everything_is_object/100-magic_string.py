#!/usr/bin/python3
def magic_string():
    num = getattr(magic_string, 'n', 0) + 1
    return (("BestSchool, " * (num + 1)) + "BestSchool")
