#!/usr/bin/python3
"""
LockedClass definitions
"""


class LockedClass:
    '''
    Python class `LockedClass` with no attributes that prevents the user from
    dynamically creating any new instance attributes not called `first_name`.
    '''
    __slots__ = ["first_name"]
