#!/usr/bin/python3

def safe_print_division(a, b):
    """Divide 2 integers and print the result.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        The Division result or None.
    """
    divResult = 0
    try:
        divResult = a / b
    except ZeroDivisionError:
        divResult = None
    finally:
        print("Inside result: {}".format(divResult))
    return (divResult)
