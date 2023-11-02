#!/usr/bin/python3
if __name__ == "__main__":

    #this block allows you to write code that can be both run as a sript and imported as module
    #the __name__ contains the name of the variable  and if set to __main__ then its been run as script
    #otherwise the current module is imported as module

    from add_0 import add

    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
