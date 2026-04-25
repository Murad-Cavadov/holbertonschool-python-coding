#!/usr/bin/python3
"""Module 7-rectangle"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    __init_subclass__ = None

    def __init__(self, width, height):
        """Initialize"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area"""
        return self.__width * self.__height

    def __str__(self):
        """String representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
