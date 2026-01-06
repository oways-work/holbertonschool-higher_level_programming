#!/usr/bin/python3
"""
Module for CountedIterator class
"""


class CountedIterator:
    """
    A class that wraps an iterator and tracks the number of items iterated.
    """
    def __init__(self, data):
        """
        Initialize the iterator and counter.
        """
        self.iterator = iter(data)
        self.counter = 0

    def get_count(self):
        """
        Return the current number of items iterated.
        """
        return self.counter

    def __next__(self):
        """
        Fetch the next item and increment the counter.
        Raises StopIteration if no items are left.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
