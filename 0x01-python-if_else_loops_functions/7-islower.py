#!/usr/bin/python3
''' function that checks for lowercase character'''


def islower(c):
    for i in range(97, 123):
        if (ord(c) == i):
            return (True)
    return (False)
