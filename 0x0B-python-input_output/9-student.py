#!/usr/bin/python3
"""Class student that defines a student by first_name, last_name and age"""


class Student:
    """class defination"""

    def __init__(self, first_name, last_name, age):
        """instantiation of the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """public class method that retrieves a dictionary representation"""
        return self.__dict__
