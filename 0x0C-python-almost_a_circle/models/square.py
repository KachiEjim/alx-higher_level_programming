#!/usr/bin/python3
"""Defines a Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initalizes the attributes

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns str rep of the square."""
        value = f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
        return value

    @property
    def size(self):
        """Returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
                "id": self.id, "x": self.x,
                'size': self.size, "y": self.y,
                }