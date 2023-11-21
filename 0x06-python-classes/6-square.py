#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of postion
        Returns:
            the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 posotive integers")
        self.__position = value

    def area(self):
        """
        finds area of square
        Returns:
            The area of the square
        """

        return (self.__size * self.__size)

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
