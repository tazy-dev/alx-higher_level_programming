#!/usr/bin/python3
def max_integer(my_list=[]):
    '''Finds the biggest integer of a list.'''
    if my_list:
        max = 0
        for num in (my_list):
            if num > max:
                max = num
        return (max)
    return (None)
