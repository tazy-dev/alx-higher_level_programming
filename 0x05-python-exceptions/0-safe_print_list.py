#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elememts of a list.

    Args:
        my_list (list): List containing elements.
        x (int): he number of elements to be printed.

    Returns:
        The actual number of elements printed.
    """
    length = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            length += 1
        except IndexError:
            break
    print("")
    return (length)
