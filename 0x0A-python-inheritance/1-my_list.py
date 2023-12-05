#!/usr/bin/python3
"""Defines class MyList that inherites from list class."""


class MyList(list):
    """MyList Class inherits from less and define
    sorted list functionality."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
