#!/usr/bin/python3
""" creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file"""
    with open(filename, 'r') as file:
        my_obj = json.loads(file.read())
        return my_obj
