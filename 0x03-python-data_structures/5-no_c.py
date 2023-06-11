#!/usr/bin/env python3
def no_c(my_string):
    '''removes all characters c and C from a string'''
    a = []
    for i in my_string:
        if i != 'c' and i != 'C':
            a.append(i)
    return (''.join(a))
