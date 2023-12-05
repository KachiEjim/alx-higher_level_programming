#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Read from a file and print it to stdout

    args:
        filename (File): File containing value to be printed
    """
    with open(filename, "r", encoding='utf-8') as f:
        value = f.read()
        print(value, end="")
