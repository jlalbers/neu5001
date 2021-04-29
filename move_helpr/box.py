# ------------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Final Project Classes: Boxes
#
# Box class and methods for final project
# ------------------------------------------------------------------------------

import qrcode
import item
from item import Item

class Box:

    def __init__(self, box_number, box_room, box_items=[]):
        if not isinstance(box_number, int):
            raise TypeError('Argument box_number must be type int')
        elif not isinstance(box_room, str):
            raise TypeError('Argument box_room must be type str')
        elif len(box_room) == 0:
            raise ValueError('Argument "box_room" must not be empty')
        elif not isinstance(box_items, list):
            raise TypeError('Argument box_items must be type list')
        elif isinstance(box_items, list):
            for element in box_items:
                if not isinstance(element, Item):
                    raise TypeError('Elements in box_items must be Item objects')
        self.box_number = box_number
        self.box_room = box_room
        self.box_items = box_items
        value_sum = 0
        for item in box_items:
            value_sum += item.get_value()
        self.box_value = value_sum


    def get_number(self):
        return self.box_number


    def get_room(self):
        return self.box_room


    def get_items(self):
        return self.box_items


    def update_value(self):
        value_sum = 0
        for item in self.box_items:
            value_sum += item.get_value()
        self.box_value = value_sum


    def get_value(self):
        self.update_value()
        return self.box_value


    def add_item(self, new_item):
        if not isinstance(new_item, Item):
            raise TypeError            
        else:
            self.box_items.append(new_item)
            self.update_value()
        

    def remove_item(self, old_item):
        if isinstance(old_item, Item):
            self.box_items.remove(old_item)
            self.update_value()
        else:
            raise TypeError


    def __str__(self):
        self.update_value()
        text = ('Box #: ' + str(self.box_number) +
        '\nValue: ' + str(self.box_value) +
        '\nRoom: ' + self.box_room + 
        '\nItems:')
        for item in self.box_items:
            text += '\n  -' + item.get_name() + ' x ' + str(item.get_quantity())
        return text
