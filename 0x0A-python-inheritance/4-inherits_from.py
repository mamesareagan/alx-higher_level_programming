#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    '''checks if object is subclass of a_class


    Args:
        obj (any): The object to check.
        a_class (type): The super class.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    '''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return(False)
