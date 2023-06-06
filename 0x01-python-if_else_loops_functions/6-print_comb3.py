#!/usr/bin/python3
''' prints all possible different combinations
of two digits
The two digits must be different
Print only the smallest combination of two digits
'''
for i in range(0, 9):
    for j in range(i + 1, 10):
        if (i == 8) and (j == 9):
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
