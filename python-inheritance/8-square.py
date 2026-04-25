#!/usr/bin/python3
"""Module 8-square"""
Rectangle = __import__('7-rectangle').Rectangle


class Square(Rectangle):
    """Class Square"""
    __init_subclass__ = None

    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area"""
        return self.__size ** 2
