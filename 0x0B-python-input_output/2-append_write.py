#!/usr/bin/python3
"""Function that appends a str to the end of a file"""

def append_write(filename="", text=""):
    """Opens a file in append mode, append to it and returns the value appended 

    args:
        filename (File): file to be created or appended to
        text (str): string to be appended to the file
    Returns: Return the number of characters appended.
    """
    with open(filename, "a", encoding='utf-8') as f:
        return (f.write(text))
