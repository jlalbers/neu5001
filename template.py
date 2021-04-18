# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Final Project Classes
#
# Classes and methods for final project
# -----------------------------------------------------------------------------
import math

def convert_to_number(s):
    return int.from_bytes(s.encode(), 'little')

class Item:
    def __init__(self, name, value=0.0, quantity=1, serial=None,
        picture=None, box=None):
        self.name = name
        self.id = convert_to_number(name)


print(convert_to_number('jeremy'))