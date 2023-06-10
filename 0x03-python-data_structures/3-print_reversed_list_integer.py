#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    le = len(my_list) - 1
    while le >= 0:
        print('{}'.format(my_list[le]))
        le -= 1
