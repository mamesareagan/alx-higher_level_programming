#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    '''print name function

        Args:
            first_name(string): first name
            last_name(string): second name
        Raises:
            TypeError: if either arguments is not string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f'My name is {first_name} {last_name}')
