#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The function 'add_integer' handles integers and floats,
casting floats to integers before the addition.
"""


def add_integer(a, b=98):
    """
    Adds 2 integers.

    Args:
        a: The first number (integer or float).
        b: The second number (integer or float), defaults to 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
