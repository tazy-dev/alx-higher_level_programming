#!/usr/bin/python3
def no_c(my_string: str):
    new_string = []
    for char in my_string:
        if char not in 'Cc':
            new_string.append(char)
    return ("".join(new_string))
