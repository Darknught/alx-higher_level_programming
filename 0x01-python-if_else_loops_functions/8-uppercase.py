#!/usr/bin/python3
def uppercase(str):
    for hy in str:
        if ord(hy) >= 97 and ord(hy) >= 122:
            hy = chr(ord(hy) - 32)
            print("{:s}".format(hy), end='')
        print('\n', end="")
