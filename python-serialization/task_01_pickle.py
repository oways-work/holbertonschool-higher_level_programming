#!/usr/bin/python3
"""
This module contains the CustomObject class which demonstrates custom
serialization and deserialization using the pickle module.
"""
import pickle


class CustomObject:
    """A custom class that can be serialized and deserialized."""

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject with name, age, and is_student.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a specific format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save to.

        Returns:
            None if an exception occurs.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject: The deserialized instance, or None if failed.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
