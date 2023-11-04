#!/usr/bin/python3

def no_c(my_string):

    del my_string["c", "C"]
    for i in my_string:
        return my_string
