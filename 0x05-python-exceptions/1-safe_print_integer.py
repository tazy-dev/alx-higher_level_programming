#!/usr/bin/python3

def safe_print_integer(value):
    """
    Print an integer with "{:d}".format().

    Args:
        value (any): Element of any type.

    Returns:
        True if vlaue is int , False othetwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) :
        return (False)
