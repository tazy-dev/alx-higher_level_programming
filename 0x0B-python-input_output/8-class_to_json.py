#!/usr/bin/python3
'''
acquire  the dictionary description for object json encoding
'''


def class_to_json(obj):
    '''
    function that returns the dictionary description with simple data structure
    for JSON serialization of an object:
    Args:
    obj: instance of a class

    Return:
    The dictionary description of the object
    '''
    return (obj.__dict__)
