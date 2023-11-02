#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import __all__

    mycount = len(sys.argv) - 1
    a = int(sys.argv[1])
    b = int(sys.argv[3]
    op = ["+", "-", "*", "/"]

    if mycount != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in list(op.keys()):
        print("Unknown operator. Available operators: +, -, * and /")

    print("{} {} {} = {}".format(a, sys.argv[2], b, op[sys.argv[2]](a, b)))
