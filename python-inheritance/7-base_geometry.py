#!/usr/bin/python3
"""This module defines the BaseGeometry class."""


class BaseGeometry:
    """A class that represents base geometry logic."""

    def area(self):
        """Raises an Exception because the area is not implemented yet."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
