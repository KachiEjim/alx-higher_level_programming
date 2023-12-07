#!/usr/bin/python3
"""a function that inserts a line of text to a file,
 after each line containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """defines a function that addeds a text after each line containing
    a specific str

    args:
        filename (file): file to be written to
        search_string (str): string to be searched in each line
        new_string (str): str to be written a line below when search_string
        is found.
        """

    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + "\n")
