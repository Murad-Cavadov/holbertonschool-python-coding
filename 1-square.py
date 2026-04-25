#!/usr/bin/python3
"""Modul ki, Square (Kvadrat) sinfini təyin edir."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size=0):
        """Yeni bir Kvadrat obyekti yaradır.

        Args:
            size (int): Kvadratın ölçüsü (default olaraq 0).

        Raises:
            TypeError: Əgər size integer deyilsə.
            ValueError: Əgər size 0-dan kiçikdirsə.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
