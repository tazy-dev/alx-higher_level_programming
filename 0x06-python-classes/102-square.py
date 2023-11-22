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
        self.__size = size

    @property
    def size(self):
        '''
        Get the value of size
        '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''
        Set the value of size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''
        Returns the current square area
        '''
        return (self.__size * self.__size)

    def __eq__(self, other) -> bool:
        """Define the == comparision to a Square."""
        return (self.__size == other.__size)

    def __ne__(self, other) -> bool:
        """Define the != comparision to a Square."""
        return (self.__size != other.__size
                )

    def __lt__(self, other) -> bool:
        """Define the < comparision to a Square."""
        return (self.__size < other.__size)

    def __le__(self, other) -> bool:
        """Define the <= comparision to a Square."""
        return (self.__size <= other.__size)

    def __gt__(self, other) -> bool:
        """Define the > comparision to a Square."""
        return (self.__size > other.__size)

    def __eq__(self, other) -> bool:
        """Define the == comparision to a Square."""
        return (self.__size == other.__size)

    def __ge__(self, other) -> bool:
        """Define the >= comparision to a Square."""
        return self.__size >= other.__size
