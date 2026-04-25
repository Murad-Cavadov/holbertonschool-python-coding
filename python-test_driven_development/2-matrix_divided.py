#!/usr/bin/python3
"""
Bu modul matrisi bolmek ucun funksiyani ehtiva edir.
"""


def matrix_divided(matrix, div):
    """
    Matrisin butun elementlerini div-e bolur.

    Args:
        matrix: Tam ve ya onluq ededlerden ibaret siyahilarin siyahisi.
        div: Bolen eded (int ve ya float).

    Returns:
        Yuvarlaqlasdirilmis neticelerden ibaret yeni matris.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Matrisin tipini ve bos olmamasini yoxlayiriq
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    # 2. Div yoxlamalari
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 3. Setirlerin eyni olcude olmasi ve elementlerin tipi
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 4. Yeni matrisin yaradilmasi
    return [[round(x / div, 2) for x in row] for row in matrix]
