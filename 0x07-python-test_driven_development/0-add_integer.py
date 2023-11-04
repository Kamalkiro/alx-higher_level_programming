#!/usr/bin/python3
"""
This script defines a fnct for integer addition.
"""


def add_integer(a, b=98):
    """
    This fnct returns the integer addition of a & b.

    If either a or b is a non-integer & non-float, TypeError is raised.
    Float arguments are typecasted.
    """

    # Check if a is not an integer or a float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is not an integer or a float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers and return their sum
    return int(a) + int(b)
