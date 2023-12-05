#!/usr/bin/python3
"""Defines a function to create an object from json file"""
import json


def load_from_json_file(filename):
    '''
    creates an Object from a “JSON file”

    Args:
    filename: The file path
    '''
    with open(filename) as file:
        return (json.load(file))
