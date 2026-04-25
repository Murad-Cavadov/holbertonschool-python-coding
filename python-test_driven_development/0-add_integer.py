#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """Adds two integers after casting floats to ints."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # NaN və Infinity yoxlaması
    if a != a or a == float('inf') or a == float('-inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == float('-inf'):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
