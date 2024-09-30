#!/usr/bin/python3
""" returns an object represented by a JSON string"""
import json


def to_json_string(my_obj):
    """ returns an object represented by a JSON string"""
    return json.loads(my_obj)
