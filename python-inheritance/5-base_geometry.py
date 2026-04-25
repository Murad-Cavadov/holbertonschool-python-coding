#!/usr/bin/python3
"""Module 5-base_geometry"""


class BaseGeometry:
    """Class BaseGeometry"""
    __init_subclass__ = None

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
