#!/usr/bin/python3
import sys
import traceback


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
        trace = list(traceback.format_exc().split(":"))[-1][1:-2]
        print("Exception: {}".format(trace), file=sys.stderr)
        return (False)
