#!/usr/bin/python3
"""Defines a function to write to a file"""


def write_file(filename="", text=""):
    '''
    Print the number of chars written tp the file.

    Args:
    filename: the file path
    text: the string to be written to the file
    '''
    with open("filename", 'a', encoding='utf-8') as file:
        print(file.write(text))
