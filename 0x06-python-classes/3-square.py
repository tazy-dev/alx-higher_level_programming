#!/usr/bin/python3
'''
A class defining a square
'''


class Square:
    '''
    A Square class
    '''

    def __init__(self, size=0) -> None:
        '''
        Intialize a Square object

        Args:
            size (int): The size of the new square object
        '''
        if not isinstance(size, int):
            raise TypeError("must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''
        Returns the current square area
        '''
        return (self.__size * self.__size)
