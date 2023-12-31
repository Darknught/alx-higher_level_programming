#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """

        Args:
            size (int): The size of the new square.
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds area of square
        Returns:
            The area of the square
        """

        return self.__size ** 2
