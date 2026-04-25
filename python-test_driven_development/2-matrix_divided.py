#!/usr/bin/python3
"""
Bu modul matrisi bolmek ucun funksiyani ehtiva edir.
"""


def matrix_divided(matrix, div):
    """
    Matrisin butun elementlerini div-e bolur.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    # 1. Matrisin tipini ve daxilindeki elementlerin tipini yoxlayiriq
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    # 2. Setirlerin olcusunu yoxlayiriq
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # 3. 'div' yoxlamalari
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 4. Yeni matris yaradiriq
    return [[round(x / div, 2) for x in row] for row in matrix]
