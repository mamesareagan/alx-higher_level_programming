#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    '''returns a list of available attributes and methods of an object


    Args:
        obj(class) : object instance
    '''

    return (dir(obj))
