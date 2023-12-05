#!/usr/bin/python3
"""Defines a function to write to a file"""


def append_write(filename="", text=""):
    '''
    Appends a string to the end of a UTF8 text file

    Args:
    filename: the file path
    text: the string to be written to the file

    Return:
    The number of characters appended
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
