#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Get the comdline arguments

    mycount = len(sys.argv) - 1

    # len is used to calculate the number of arguments

    if mycount == 0:
        print("0 arguments.")
    elif mycount == 1:
        print("1 argument.")
    else:
        print("{} arguments".format(mycount))

        # the for loop is to iterate over sys.argv nd print each arg on newline
        # i + 1 is used to represent the index of current arg
        # sys.argv is used to access the value of current arg

    for i in range(mycount):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
