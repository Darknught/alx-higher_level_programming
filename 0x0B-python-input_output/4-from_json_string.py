#!/usr/bin/python3
"""Defines a function that returns an object represented by JSON"""


import json


def from_json_string(my_str):
    """Initialization of the function"""
    return json.loads(my_str)
