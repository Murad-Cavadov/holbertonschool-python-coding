#!/usr/bin/python3
"""
Bu modul iki tam ədədi toplayan add_integer funksiyasını ehtiva edir.
Funksiya float dəyərləri qəbul edir və onları tam ədədə çevirir.
"""


def add_integer(a, b=98):
    """
    İki ədədi (a və b) toplayır və nəticəni tam ədəd kimi qaytarır.

    Arqumentlər:
        a: integer və ya float
        b: integer və ya float (susmaya görə 98)

    Returns:
        İki ədədin tam ədəd kimi cəmi.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # NaN və Infinity yoxlaması (isinstance(a, float) artıq yuxarıda yoxlanıb)
    if a != a or a == float('inf') or a == -float('inf'):
        raise TypeError("a must be an integer")
    if b != b or b == float('inf') or b == -float('inf'):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
