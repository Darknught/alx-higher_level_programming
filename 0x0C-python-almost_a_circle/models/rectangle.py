#!/usr/bin/python3
"""Module that inherits properties from base class"""
from .base import Base


class Rectangle(Base):
    """class definition of rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of class with private instance attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Property getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Property getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Property getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter function for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns area value of Rectangle instance"""
        return self.width * self.height

    def display(self):
        """public method that prints in stdout Rectangle instance with #"""
        for i in range(self.y):
            print()
        for i in range(self.__height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Public method to update attributes of the rectangle"""
        if args:
            # If *args exists and not empty, assign values based on positions
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
            # If *args is empty or not provided, assign val based on **kwargs
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """Overriden __str__ method to craete a string representation"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )

    def to_dictionary(self):
        """public method to return dictionary representation of rectangle"""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
