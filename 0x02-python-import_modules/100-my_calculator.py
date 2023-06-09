#!/usr/bin/python3
if  __name__ == '__main__':
    import calculator_1 as c
    import sys as s
    if (len(s.argv) != 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        s.exit(1)
    a = int(s.argv[1])
    b = int(s.argv[3])
    if (s.argv[2] == '+'):
        print('{} + {} = {}'.format(a, b, c.add(a, b)))
        s.exit(0)
    elif (s.argv[2] == '-'):
        print('{} - {} = {}'.format(a, b, c.sub(a, b)))
        s.exit(0)
    elif (s.argv[2] == '*'):
        print('{} * {} = {}'.format(a, b, c.mul(a, b)))
        s.exit(0)
    elif (s.argv[2] == '/'):
        print('{} / {} = {}'.format(a, b, c.div(a, b)))
        s.exit(0)
    else:
        print ('Unknown operator. Available operators: +, -, * and /')
        s.exit(1)
