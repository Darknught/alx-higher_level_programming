#!/usr/bin/python3
"""Module that inherits properties from base class"""
from .base import Base


class Rectangle(Base):
    """class definition of rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of class with private instance attributes"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
