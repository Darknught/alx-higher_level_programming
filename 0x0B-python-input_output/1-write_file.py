#!/usr/bin/python3
"""Defines a function that writes string to a text file"""


def write_file(filename="", text=""):
    """Initialization of the function
    Returns:
        number of chars written to "filename" from "text"
    """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
