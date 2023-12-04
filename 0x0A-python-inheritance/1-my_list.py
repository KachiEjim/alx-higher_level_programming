#!/usr/bin/python3
"""A class MyList that inherits from list"""


class MyList(list):
    """A custom list class inheriting from the built-in list class.

    Args:
        list (class): The built-in list class used for inheritance.

    Attributes:
        Inherits all attributes and methods from the built-in list class.

    """

    def print_sorted(self):
        """Prints the elements of the list in ascending order.

        Sorts the list in ascending order and prints it.

        Example:
            >>> my_list = MyList([5, 2, 9, 1, 7])
            >>> my_list.print_sorted()
            [1, 2, 5, 7, 9]

        """
        print(sorted(self))
