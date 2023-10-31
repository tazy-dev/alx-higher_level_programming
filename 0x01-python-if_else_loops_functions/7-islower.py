#!/usr/bin/python3
def islower(c: str):
    '''Checks id c is lower case returning Ture or false'''
    if ord(c) >= 97 and ord(c) <= 123:
        return True
    return False
