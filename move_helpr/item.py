# ------------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Final Project Classes: Items
#
# Item class and methods for final project
# ------------------------------------------------------------------------------

# convert_to_number function created by Stack Overflow user poke, originally
# posted at: https://stackoverflow.com/questions/31701991/
# string-of-text-to-unique-integer-method
def convert_to_number(s: str) -> int:
    return int.from_bytes(s.encode(), 'little')

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
