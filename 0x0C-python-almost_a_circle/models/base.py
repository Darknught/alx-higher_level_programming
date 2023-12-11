#!/usr/bin/python3
"""Module that defines a class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
