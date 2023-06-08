#!/usr/bin/python3
if __name__ == '__main__':
    import sys as s
    length = len(s.argv) - 1
    if length != 1:
        if length == 0:
            print('{} arguments.'.format(length))
        else:
            print('{} arguments:'.format(length))
    else:
        print('{} argument:'.format(length))
    for i in range(1, (length + 1)):
        print("{}: {}".format(i, s.argv[i]))
