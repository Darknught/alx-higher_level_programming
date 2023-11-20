#!/usr/bin/python3

def safe_print_integer(value):
    if value == True:
        return True
    else:
        return False
    try:
        print("{:d}".format(value))
    except ValueError:
        return value
