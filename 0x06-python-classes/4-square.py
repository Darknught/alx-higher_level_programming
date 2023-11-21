#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    def area(self):
        """
        finds area of square
        Returns:
            The area of the square
        """

        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a square
        Retuens:
            None
        """

        if type(value) is not int:
            raise TypeError('size must be an integer')
        else:
            if value < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = value
