#!/usr/bin/python3
"""Defines function that returns JSON representation of an object(string)"""


import json


def to_json_string(my_obj):
    """Initialization of the function"""
    return json.dumps(my_obj)
