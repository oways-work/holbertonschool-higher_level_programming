#!/usr/bin/python3
"""
This module provides a function `print_square` that prints
a square of a given size using the '#' character.
"""


def print_square(size):
      """
          Prints a square with the character #.

              Args:
                      size: The length of the side of the square.

                          Raises:
                                  TypeError: If size is not an integer.
                                          ValueError: If size is less than 0.
                                                  TypeError: If size is a float and is less than 0.
                                                      """
      if not isinstance(size, int):
                if isinstance(size, float) and size < 0:
                              raise TypeError("size must be an integer")
                          if not isinstance(size, float):
                                        raise TypeError("size must be an integer")
                                    # If it's a positive float, it still must be an integer
                                    raise TypeError("size must be an integer")

      if size < 0:
                raise ValueError("size must be >= 0")

      for _ in range(size):
                print("#" * size)
