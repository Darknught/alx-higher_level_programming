#!/usr/bin/python3
"""Class student that defines a student by first_name, last_name and age"""


class Student:
    """class defination"""

    def __init__(self, first_name, last_name, age):
        """instantiation of the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """public class method that retrieves a dictionary representation
        Args:
            if attrs is a list of strings, only attribute names contained
            in this list must be retrieved
        Otherwise:
            All attributes must be retrieved
        """
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_fom_json(self, json):
        """pulic method that replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
