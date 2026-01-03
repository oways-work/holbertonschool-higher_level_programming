#!/usr/bin/python3
"""Defines a function that finds the biggest integer of a list."""


def max_integer(my_list=[]):
    """Finds the biggest integer of a list."""
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for i in my_list:
        if i > max_val:
            max_val = i
    return max_val
