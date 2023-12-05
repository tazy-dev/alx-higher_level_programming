#!/usr/bin/python3
"""Defines a function to write to a file"""


def write_file(filename="", text=""):
    '''
     rite a string to a UTF8 text file..

    Args:
    filename: the file path
    text: the string to be written to the file

    Return:
    The number of characters written
    '''
    with open(filename, 'w', encoding="utf-8") as file:
        return (file.write(text))
