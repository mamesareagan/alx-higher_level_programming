#!/usr/bin/python3
def lookup(obj):
    '''returns a list of available attributes and methods of an object


    Args:
        obj(class) : object instance
    '''

    return (dir(obj))
