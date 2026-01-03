#!/usr/bin/python3
"""Defines a function that multiplies values by 2."""


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""
    return {key: value * 2 for key, value in a_dictionary.items()}
