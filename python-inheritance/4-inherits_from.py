#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance of a class that inherited
        (directly or indirectly) from a_class; otherwise False.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
