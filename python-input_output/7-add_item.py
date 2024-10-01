#!/usr/bin/python3
""" writes an Object to a text file, using a JSON representation"""
import json


from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file
filename = "add_item.json"

try:
    new_list = load_from_json_file(filename)
except FileNotFoundError:
    new_list = []

new_list.extend(words[1:])

save_to_json_file(new_list, filename)