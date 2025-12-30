#!/usr/bin/python3
"""
This module provides the fizzbuzz function for printing numbers with specific
replacement rules.
"""


def fizzbuzz():
    """
    Prints the numbers from 1 to 100 separated by a space.
    For multiples of three print Fizz.
    For multiples of five print Buzz.
    For numbers which are multiples of both three and five print FizzBuzz.
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
