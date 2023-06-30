#!/usr/bin/python3
'''doctest in tests/0-add_integer.txt'''


def add_integer(a, b=98):
    '''Returns sum
    a + b
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
