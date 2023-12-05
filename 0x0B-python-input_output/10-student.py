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

    def to_json(self, attrs=None):
        ''' Returns a dictionary representation of a Student instance

        Args:
        attrs: List containg the attributes to be returned if found
        '''
        if (type(attrs) is list and
                all(type(attr) issubclass str for attr in attrs)):
            return {k: self.__getattribute__(k) for k in attrs
                    if hasattr(self, k)}
        return (self.__dict__)
