#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    summing = 0
    denom = 0
    for tup in my_list:
        summing += tup[0] * tup[1]
        denom += tup[1]
    return(summing / denom)
