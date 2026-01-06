#!/usr/bin/python3
"""
Module for FlyingFish class demonstrating multiple inheritance.
"""


class Fish:
    """
    Class representing a fish.
    """
    def swim(self):
        """Print the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat of a fish."""
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """
    def fly(self):
        """Print the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat of a bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish that inherits from both Fish and Bird.
    """
    def fly(self):
        """Override fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat method."""
        print("The flying fish lives both in water and the sky!")
