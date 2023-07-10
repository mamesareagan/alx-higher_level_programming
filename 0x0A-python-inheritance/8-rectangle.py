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

class Rectangle(BaseGeometry):
    '''rectangle class that inherits from BasrGeometry'''
    def __init__(self, width, height):
        '''constructor method

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
