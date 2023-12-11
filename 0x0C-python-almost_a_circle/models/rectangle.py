#!/usr/bin/python3
"""Rectangle Class that inherits from base"""
from models.base import Base


class Rectangle(Base):
    """Defines the class Rectangle

    args:
        Base (class): A definition of the class base.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initalizes an instance of the class
        
        args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): parameter x
            y (int): parameter y
            id (int): parameter id

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the rectangle instance"""
        return self.height * self.width

    def display(self):
        """Prints the Rectangle to stdout"""
        for _ in range(self.y):
            print()
        [print(" " *self.x + "#" * self.width) for _ in range(self.height)]

    def __str__(self):
        result = f"[Rectangle] ({self.id}) {self.x}/{self.y} "
        result += f"- {self.width}/{self.height}"
        return (result)

    def update(self, *args, **kwargs):
        """Used to update the class Rectangle"""
        if args and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]

        else:
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value


    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {
            "x": self.x, "y": self.y,
            "id": self.id, 'height': self.height,
            "width": self.width
        }
