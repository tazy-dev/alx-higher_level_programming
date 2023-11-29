#!/usr/bin/python3
"""Defines an print_square function."""


def print_square(size):
    """
    Prints a square with the character #

     Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for idx in range(size):
        print("#" * size)
