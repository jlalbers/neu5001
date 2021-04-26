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
# def convert_to_number(s: str) -> int:
#   return int.from_bytes(s.encode(), 'little')

class Item:

    def __init__(self, name, value=0.0, quantity=1, serial='',
        picture='', box=0):
        if not isinstance(name, str):
            raise TypeError('Argument "name" must be type str')
        elif not isinstance(value, (int, float)):
            raise TypeError('Argument "value" must be type int or float')
        elif value < 0:
            raise ValueError('Value of argument "value" must be at least 0')
        elif not isinstance(quantity, int):
            raise TypeError('Argument "quantity" must be type int')
        elif quantity < 1:
            raise ValueError('Value of rgument "quantity" must be at least 1')
        elif not isinstance(serial, str):
            raise TypeError('Argument "serial" must be type str')
        elif not isinstance(picture, str):
            raise TypeError('Argument "picture" must be type str')
        elif not isinstance(box, int):
            raise TypeError('Argument "box" must be type int')
        elif box < 0:
            raise ValueError('Value of argument "box" must be at least 0')
        self.name = name.lower()
        self.id = int.from_bytes(name.encode(), 'little')
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
        if not isinstance(new_name, str):
            raise TypeError('Argument "new_name" must be type str')
        else:
            self.name = new_name.lower()
            self.id = int.from_bytes(new_name.encode(), 'little')


    def update_value(self, new_value):
        if not isinstance(new_value, (int, float)):
           raise TypeError('Argument "new_value" must be type int or float')
        elif new_value < 0:
            raise ValueError('Value of argument "new_value" must be at least 0')
        else:
            self.value = new_value


    def update_quantity(self, new_quantity):
        if not isinstance(new_quantity, int):
            raise TypeError('Argument "new_quantity" must be type int')
        elif new_quantity < 1:
            raise ValueError('Value of argument "new_quantity" must be at least 1')
        else:
            self.quantity = new_quantity


    def update_serial(self, new_serial):
        if isinstance(new_serial, str):
            self.serial = new_serial
        else:
            raise TypeError('Argument "new_serial" must be type str')


    def update_picture(self, new_picture):
        if not isinstance(new_picture, str):
            raise TypeError('Argument "new_picture" must be type str')
        else:
            self.picture = new_picture


    def update_box(self, new_box):
        if not isinstance(new_box, int):
            raise TypeError('Argument "new_box must be type int')
        elif new_box < 0:
            raise ValueError()
        else:
            self.box = new_box
    

    def __str__(self):
        output = ('Item Name: ' + self.get_name() +
            '\n\tID #: ' + str(self.get_id()) +
            '\n\tValue: $' + str(self.get_value()) +
            '\n\tQuantity: ' + str(self.get_quantity()) +
            '\n\tSerial #: ' + self.get_serial() +
            '\n\tPicture: ' + self.get_picture() +
            '\n\tBox #: ' + str(self.get_box()))
        return output
