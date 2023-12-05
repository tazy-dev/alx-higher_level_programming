#!/usr/bin/python3
"""Defines a class and parent classes checking function."""


def inherits_from(obj, a_class: type) -> bool:
    """Check if an object is an instance  of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
