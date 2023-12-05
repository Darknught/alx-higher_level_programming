#!/usr/bin/python3
"""Defines a function that reads a text file UTF8 and prints to stdout"""


def read_file(filename=""):
    """Initialization of the function that reads from "filename" """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
