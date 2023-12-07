#!/usr/bin/python3
"""Module that defines a class"""


class Base:
    """class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class
        Args:
            id - if id is not None, and if so assign it to the public
            instance attribute; otherwise, increment __nb_objects and
            assign the new value to the public instance attribute id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
