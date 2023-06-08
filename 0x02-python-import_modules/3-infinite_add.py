#!/usr/bin/python3
if __name__ == "__main__":
    '''prints the result of the addition of all arguments'''
    import sys as s
    suma = 0
    le = len(s.argv)
    for i in range(1, le):
        suma += int(s.argv[i])
    print('{}'.format(suma))
