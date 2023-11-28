#!/usr/bin/python3
def magic_string():
    magic_string.idx = getattr(magic_string, 'idx', 0) + 1
    return ("BestSchool, " * (magic_string.idx - 1) + "BestSchool")
