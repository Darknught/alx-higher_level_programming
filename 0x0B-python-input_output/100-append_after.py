#!/usr/bin/python3
"""Contains function that inserts a line of text to a file
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """initialization of the function"""
    with open(filename, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    for line in lines:
        modified_lines.append(line)
        if search_string in line:
            modified_lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(modified_lines)
