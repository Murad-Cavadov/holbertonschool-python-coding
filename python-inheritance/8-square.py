#!/usr/bin/python3
"""
Module 8-square
Defines a class Square that inherits from Rectangle
"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square's side.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
