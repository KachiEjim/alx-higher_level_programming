#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    number_of_instances = 0
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculates and returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        """ a class Rectangle that defines a rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip("\n")

    def __repr__(self):
        """Defines and returns a string rep of a rectangle"""
        new = f"Rectangle({str(self.__width)}, {str(self.__height)})"
        return (new)

    def __del__(self):
        """Print the message Bye rectangle...
        when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1
