#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    result = 0

    # range is used to loop over sys.argv and the -1 skips the first element
    # which is the name of the program itself
    # int is used to convert the current element of sys.argv
    # the += is used to add the current element of argv to "result" variable

    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result))
