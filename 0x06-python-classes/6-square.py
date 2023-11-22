#!/usr/bin/python3
'''
A class defining a square
'''


class Square:
    '''
    A Square class
    '''

    def __init__(self, size=0, position=(0, 0)) -> None:
        '''
        Intialize a Square object

        Args:
            size (int): The size of the new square object
            position (tuple): The starting location of the square
        '''
        self.__size = size
        self.__position = position

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
            raise TypeError("must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''
        Get the value of position attribute
        '''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''
        Set the value of position attribute
        '''
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all([isinstance(num, int) for num in value]) or
                not all([num >= 0 for num in value])):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''
        Returns the current square area
        '''
        return (self.__size * self.__size)

    def my_print(self):
        '''
        prints the square with the character `#` to standard output
        (if `size` == 0 -> prints an empty line
        '''
        if self.__size == 0:
            print()
            return
        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
