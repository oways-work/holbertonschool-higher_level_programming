#!/usr/bin/python3
"""Defines a function that replaces occurrences of an element."""


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    return [replace if x == search else x for x in my_list]
