#!/usr/bin/python3
'''a BaseGeometry class'''


class BaseGeometry:
    '''base  class'''
    def area(self):
        '''raises exception error'''
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        '''validates value to be an integer'''
        if value < 1:
            raise ValueError("<name> must be greater than 0")

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

