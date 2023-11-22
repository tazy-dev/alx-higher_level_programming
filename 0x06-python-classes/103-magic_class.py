#!/usr/bin/python3
'''
A class definition matching the bytecode provided
'''

import math


class MagicClass:
    '''
    A MagicClass that represent a circle
    '''

    def __init__(self, radius=0) -> None:
        '''
        Intialize a MagicClass object

        Args:
            radius (int): The radius of the new MagicClass object
        '''
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''
        Returns the current MagicClass object area
        '''
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        '''
        Returns the current MagicClass object circumference
        '''
        return (2 * math.pi * self.__radius)
