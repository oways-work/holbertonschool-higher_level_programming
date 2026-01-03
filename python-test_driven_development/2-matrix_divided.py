#!/usr/bin/python3
"""
This module provides a function `matrix_divided` that divides all elements
of a matrix by a given number.
"""


def matrix_divided(matrix, div):
      """
          Divides all elements of a matrix by div.

              Args:
                      matrix: A list of lists of integers or floats.
                              div: A number (integer or float) to divide by.

                                  Returns:
                                          A new matrix with the results rounded to 2 decimal places.

                                              Raises:
                                                      TypeError: If matrix is not a list of lists of integers/floats.
                                                              TypeError: If rows of the matrix are not of the same size.
                                                                      TypeError: If div is not a number.
                                                                              ZeroDivisionError: If div is 0.
                                                                                  """
      msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix:
              raise TypeError(msg)

    row_len = None
    for row in matrix:
              if not isinstance(row, list):
                            raise TypeError(msg)
                        if row_len is None:
                                      row_len = len(row)
elif len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
                      if not isinstance(element, (int, float)):
                                        raise TypeError(msg)

              if not isinstance(div, (int, float)):
                        raise TypeError("div must be a number")

    if div == 0:
              raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
