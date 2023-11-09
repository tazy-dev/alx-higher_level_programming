#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return None
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(roman_string)
    equivelent, i = 0, 0
    for i in range(length):
        if i > 0 and romans[roman_string[i + 1]] > romans[roman_string[i]]:
            equivelent += romans[roman_string[i]] -\
	    		2 * romans[roman_string[i]]
        else:
            equivelent += romans[roman_string[i]]
    return (equivelent)
