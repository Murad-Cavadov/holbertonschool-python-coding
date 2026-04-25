#!/usr/bin/python3
"""Module that contains the function inherits_from."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if obj inherited from a_class (but is not a_class itself),
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
