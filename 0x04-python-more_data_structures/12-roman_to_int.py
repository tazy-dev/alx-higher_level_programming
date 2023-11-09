#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return None
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string)
    equivelent, i = 0, 0
    while i < length:
        if i + 1 < length and romans[roman_string[i]] <\
                romans[roman_string[i + 1]]:
            equivelent += romans[roman_string[i + 1]] - romans[roman_string[i]]
            i += 2
        else:
            equivelent += romans[roman_string[i]]
            i += 1
    return (equivelent)
