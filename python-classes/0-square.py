#!/usr/bin/python3
"""Bu modul sadə bir Square (Kvadrat) sinfini təyin edir."""


class Square:
    """Kvadratı təmsil edən sinif."""

    def __init__(self, size):
        """Yeni bir Kvadrat obyekti yaradır.
        
        Args:
            size (int): Kvadratın ölçüsü.
        """
        self.__size = size
