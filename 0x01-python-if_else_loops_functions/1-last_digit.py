#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# gets last digit of number
last = abs(number) % 10
string = "Last digit of {} is {} and is"
if last > 5:
    print("{} greater than 5".format(string.format(number, last)))
elif (last > 0) and (last < 6):
    print("{} less than 6 and not 0".format(string.format(number, last)))
else:
    print("{} 0".format(string.format(number, last)))
