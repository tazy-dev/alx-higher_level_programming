#!/usr/bin/python3
"""Defines a function to make object from json"""
import json


def from_json_string(my_str):
    '''
    t returns an object (Python data structure) represented by a JSON string

    Args:
    my_str: the object as a json String
    '''
    return (json.loads(my_str))
