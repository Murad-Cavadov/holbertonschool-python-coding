#!/usr/bin/python3
"""
Module 7-rectangle
Defines a class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a new Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
