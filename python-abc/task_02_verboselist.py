#!/usr/bin/python3
"""
Module for VerboseList class
"""


class VerboseList(list):
    """
    A custom list class that notifies when items are added or removed.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable
        and print a notification.
        """
        # Convert iterable to list to count items safely if needed,
        # or simply rely on the count of items added.
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """
        Remove the first item from the list whose value is equal to x
        and print a notification.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove the item at the given position in the list, and return it.
        Print a notification before popping.
        """
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
