#!/usr/bin/python3
"""
Bu modul print_square funksiyasini ehtiva edir.
"""


def print_square(size):
    """
    '#' simvolu ile kvadrat cap edir.

    Args:
        size: Kvadratin terefinin uzunlugu.

    Raises:
        TypeError: Eger size tam eded deyilse.
        ValueError: Eger size 0-dan kicikdirse.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
