#!/usr/bin/python3
'''
Define a Student Class
'''


class Student:
    '''Represent a student'''
    def __init__(self, first_name, last_name, age) -> None:
        '''Initialize new student object
        Args:
        first_name (str): student first name
        last_name (str): student last name
        age (int): student age
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ''' Returns a dictionary representation of a Student instance'''
        return (self.__dict__)
