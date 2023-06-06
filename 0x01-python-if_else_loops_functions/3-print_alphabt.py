#!/usr/bin/python3
'''program that prints the ASCII alphabet, in lowercase, not followed by a new line.'''
for i in range(97, 123):
    if (chr(i) == 'q') or (chr(i) == 'e'):
        continue
    print("{}".format(chr(i)), end='')
