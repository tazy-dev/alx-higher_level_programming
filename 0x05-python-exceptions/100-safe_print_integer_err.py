#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    Print an integer .

    Args:
        value (any): Element of any type.

    Returns:
        True if vlaue is int , False othetwise.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
