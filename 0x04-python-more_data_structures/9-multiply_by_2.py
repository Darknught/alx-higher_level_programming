#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    """
    Returns a new dictionary with all values multiplied by 2
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        a new dictionary
    """
    return {key: value * 2 for key, value in a_dictionary.items()}
