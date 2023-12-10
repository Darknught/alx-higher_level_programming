#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Fuction initialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overridden __str__ method for Square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
