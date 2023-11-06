#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    '''Finds all multiples of 2 in a list.'''
    if my_list:
        evens = []
        for num in (my_list):
            if num % 2 == 0:
                evens.append(True)
            else:
                evens.append(False)
        return (evens)
