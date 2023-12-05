#!/usr/bin/python3
"""Defines a function to make json and write it to a file"""
import json


def save_to_json_file(my_obj, filename):
    '''
    writes an Object to a text file, using a JSON representation:

    Args:
    my_obj: the object
    filename: The file path
    '''
    with open(filename, "w") as file:
        json.dump(my_obj, file)
