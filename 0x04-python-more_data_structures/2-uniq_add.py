#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        uniqe = set(my_list)
        return (sum(uniqe))
    return 0
