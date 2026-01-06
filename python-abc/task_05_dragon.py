#!/usr/bin/python3
"""
Module for Dragon class demonstrating Mixins.
"""


class SwimMixin:
    """
    Mixin class to add swimming capability.
    """
    def swim(self):
        """Print the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class to add flying capability.
    """
    def fly(self):
        """Print the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon that inherits capabilities from
    SwimMixin and FlyMixin.
    """
    def roar(self):
        """Print the roaring behavior of a dragon."""
        print("The dragon roars!")
