#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """
    A function that executes a function safely..

    Args:
        fct : Pointer to a function.

    Returns:
        The result of the function,.
    """
    try:
        funcResult = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
    else:
        return funcResult
