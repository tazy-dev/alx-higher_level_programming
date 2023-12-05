#!/usr/bin/python3
"""Defines an object lookup function."""


def lookup(obj):
    """Return a list of an object's attributes, and recursively the attributes
    of its bases class."""
    return (dir(obj))
