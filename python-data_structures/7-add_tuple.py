#!/usr/bin/python3
"""Defines a function that adds 2 tuples."""


def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples."""
    # Add (0, 0) to ensure at least 2 elements, then slice first 2
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]
    return (a[0] + b[0], a[1] + b[1])
