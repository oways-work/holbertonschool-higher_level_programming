#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to define unittests for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max value at the start of the list"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test with negative numbers in the list"""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    def test_floats_and_ints(self):
        """Test with mixed floats and integers"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

if __name__ == '__main__':
    unittest.main()
