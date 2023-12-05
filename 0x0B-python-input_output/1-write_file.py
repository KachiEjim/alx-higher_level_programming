#!/usr/bin/python3
""" a function that reads a text file (UTF8) and prints it to stdout:"""


def write_file(filename="", text=""):
    """Opens a file in write mode, write to it and returns the value written 

    args:
        filename (File): file to be created or written to
        text (str): string to be written to the file
    Returns: Return the number of characters written.
    """
    with open(filename, "w", encoding='utf-8') as f:
        return (f.write(text))