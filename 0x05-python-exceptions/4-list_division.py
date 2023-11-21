#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide 2 integers and print the result.

    Args:
        my_list_1 (list(any)): First list of elements.
        my_list_2 (list(any)): Second list of elements.
        list_length (list(any)): The number of elements in the result list.

    Returns:
        List with length = list_length with all Divisions.
    """
    resutl_list = []
    divResult = 0
    for idx in range(list_length):
        try:
            divResult = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
            divResult = 0
        except ZeroDivisionError :
            print("division by 0")
            divResult = 0
        except IndexError:
            print("out of range")
            divResult = 0
        finally:
           resutl_list.append(divResult)
    return (resutl_list)
