# ------------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Final Project Classes
#
# Classes and methods for final project
# ------------------------------------------------------------------------------
import math
import zlib
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

# convert_to_number function created by Stack Overflow user poke, originally
# posted at: https://stackoverflow.com/questions/31701991/
# string-of-text-to-unique-integer-method
def convert_to_number(s: str) -> int:
    return int.from_bytes(s.encode(), 'little')

def obscure(data: bytes) -> bytes:
    return b64e(zlib.compress(data, 9))

def unobscure(obscured: bytes) -> bytes:
    return zlib.decompress(b64d(obscured))

class Item:

    def __init__(self, name, value=0.0, quantity=1, serial=None,
        picture=None, box=None):
        self.name = name
        self.id = convert_to_number(name)
        self.value = value
        self.quantity = quantity
        self.serial = serial
        self.picture = picture
        self.box = box

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id

    def get_value(self):
        return self.value

    def get_quantity(self):
        return self.quantity

    def get_serial(self):
        return self.serial

    def get_picture(self):
        return self.picture

    def get_box(self):
        return self.box

    def update_name(self, new_name):
        self.name = new_name
        self.id = convert_to_number(new_name)

    def update_value(self, new_value):
        self.value = new_value

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def update_serial(self, new_serial):
        self.serial = new_serial

    def update_picture(self, new_picture):
        self.picture = new_picture

    def update_box(self, new_box):
        self.box = new_box


class Box:

    def __init__(self, box_number, box_items=[]):
        self.box_number = box_number
        self.box_items = box_items
        value_sum = 0
        for item in box_items:
            value_sum += item.get_value()
        self.box_value = value_sum


class User:

    def __init__(self, username, password):
        self.user = username
        self.password = obscure(password.encode())


dresser = Item('Dresser', value=500.0)
chair = Item('Chair', value=51.0)

box = Box(1, box_items=[dresser, chair])

print(box.box_value)

print(dresser.id, chair.id)

user = User('jameson', 'password')

print(user.password)