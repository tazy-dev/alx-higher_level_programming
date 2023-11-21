#!/usr/bin/python3
'''
A class defining a square
'''


class Square:
    '''
    A Square class
    '''
    def __init__(self, size) -> None:
        '''
        Intialize a Square object

        Args:
            size (int): The size of the new square object
        '''
        self.__size = size
