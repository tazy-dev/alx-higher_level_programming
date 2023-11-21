#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elememts of a list and only integers.

    Args:
        my_list (list[any]): List containing elements of any type.
        x (int): he number of elements to be printed.

    Returns:
        The actual number of integers printed.
    """
    length = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            length += 1
        except (TypeError, ValueError):
            pass
    print("")
    return (length)
