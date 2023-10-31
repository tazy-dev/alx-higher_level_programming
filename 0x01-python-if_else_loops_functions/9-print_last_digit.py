#!/usr/bin/python3
def print_last_digit(number : int):
    '''Prints the last digit of a number'''
    last_digit = abs(number) % 10
    print(f"{last_digit:d}",end="")
    return last_digit