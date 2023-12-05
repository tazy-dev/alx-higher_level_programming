#!/usr/bin/python3
"""Defines a function to make json"""
import json


def to_json_string(my_obj):
    '''
    returns the JSON representation of an object (string):.

    Args:
    my_obj: the object
    '''
    return (json.dumps(my_obj))
