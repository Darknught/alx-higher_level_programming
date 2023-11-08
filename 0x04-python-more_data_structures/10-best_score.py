#!/usr/bin/python3
def best_score(my_dict):

    """
    Returns a key with the biggest integer value
    ...

    Parameters
    ----------
    a_dictionary : dictionary
        the given dictionary

    Return:
        If no score found, return None
        Key with biggest integer value otherwise
    """

    if my_dict and len(my_dict):
        max = list(my_dict.keys())[0]
        for key in my_dict:
            if my_dict[key] > my_dict[max]:
                max = key
        return max
    return None
