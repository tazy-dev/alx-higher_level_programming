#!/usr/bin/python3
"""Defines a class and parent classes checking function."""


def is_kind_of_class(obj, a_class: type) -> bool:
    """Check if an object is  an instance of a given class or an
    instance of a class that inherited from.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return (isinstance(obj, a_class))
