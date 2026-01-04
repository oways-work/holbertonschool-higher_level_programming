#!/usr/bin/python3
"""
This module provides a function that prints a square using '#'.
It validates that the size is a non-negative integer.
"""


def print_square(size):
    """Prints a square with the character #."""
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
