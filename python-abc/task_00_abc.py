#!/usr/bin/python3
"""Module for abstract Animal class and its subclasses.

This module defines an abstract Animal class using ABC and provides
concrete implementations through Dog and Cat subclasses.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal.

    This class serves as a blueprint for all animal subclasses,
    requiring them to implement the sound method.
    """

    @abstractmethod
    def sound(self):
        """Abstract method that should return the sound of the animal.

        This method must be implemented by all subclasses.

        Returns:
            str: The sound made by the animal
        """
        pass


class Dog(Animal):
    """A Dog class that inherits from Animal.

    This class represents a dog and implements the sound method
    to return the sound a dog makes.
    """

    def sound(self):
        """Return the sound a dog makes.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """A Cat class that inherits from Animal.

    This class represents a cat and implements the sound method
    to return the sound a cat makes.
    """

    def sound(self):
        """Return the sound a cat makes.

        Returns:
            str: "Meow"
        """
        return "Meow"
