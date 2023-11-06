#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    del my_list[3]
    if idx < 0 or idx >= (len(my_list)):
        return my_list.copy()

    new = my_list.copy()
    return new
