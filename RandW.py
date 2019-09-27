#!/usr/bin/env python
import json
import os
from pprint import pprint
#
# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))
# Read in the JSON text
with open(os.path.join(here, "source_file.txt")) as file:
    json_text = file.read()
    # Display the type and contents of the json_text var
    print("json_text is a", type(json_text))
    print(json_text)
    # Use the json module to parse the JSON string into native Python data
    json_data = json.loads(json_text)
    # Display the type and contents of the json_data var
    print("json_data is a", type(json_data))
    pprint(json_data)
    print("here is interface dictionary:")
    pprint(json_data["ietf-interfaces:interface"])
    print("\nhere is IP Addr:")
    pprint(json_data["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"])

#itterating through a dictionary
fruit_inventory = {"apples": 5, "pears": 2, "oranges": 9}
for fruit, quantity in fruit_inventory.items():
    print("\nYou have {} {}.".format(quantity, fruit))
