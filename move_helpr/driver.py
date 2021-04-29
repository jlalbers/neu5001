# ------------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Final Project Driver Program
#
# Basic user interface for interacting with program.
# ------------------------------------------------------------------------------
import os
import sys
import csv
import time
import qrcode
import webbrowser
import PIL
import reportlab
import item
import box

from PIL import Image
from item import Item
from box import Box

def login(username: str) -> str:
    cwd = os.getcwd()
    if username in os.listdir(cwd):
        print('Login successful!')
        time.sleep(1)
    else:
        new_profile = '1'
        while new_profile.lower() not in ('y', 'n'):
            new_profile = input('You do not have a profile. Would you like to make one? (Y/N)\n>>>')
            print()
            if new_profile.lower() == 'y':
                new_dir = os.path.join(cwd, username)
                os.mkdir(new_dir)
            elif new_profile.upper() == 'n':
                print('Goodbye!')
                time.sleep(1)
                sys.exit()
            else:
                print('Invalid option.\n')
    return os.path.join(cwd, username)


def check_user_dir(username, dir):
    files = os.listdir(dir).copy()
    if username + '_items.csv' in files:
        items_exist = True
    else:
        items_exist = False
        new_file = open(dir + '/' + username + '_items.csv', 'w')
    '''if username + '_boxes.csv' in files:
        boxes_exist = True
    else:
        boxes_exist = False'''
    return items_exist


def get_item_file(username: str, dir: str, exist: bool):
    os.chdir(dir)
    check_item_file = username + '_items.csv'
    return_file = open(check_item_file, 'r')
    return return_file


def get_items(item_file) -> list:
    item_list = []
    if os.path.getsize(os.path.realpath(item_file.name)) != 0:
        item_reader = csv.reader(item_file, delimiter=',', quotechar='"')
        for line in item_reader:
            name, value, quantity, serial, picture, box = line
            line_item = (Item(name, float(value), int(quantity),
                serial, picture, int(box)))
            item_list.append(line_item)
    item_file.close()
    return item_list


def get_boxes(item_list) -> list:
    if len(item_list) == 0:
        output = []
    else:
        box_list = []
        box_number_set = set()
        for item_to_get in item_list:
            if item_to_get.get_box() > 0:
                box_number_set.add(item_to_get.get_box())
        for num in box_number_set:
            new_box = Box(num, 'Room TBD')
            for item_to_move in item_list:
                if item_to_move.get_box() == num:
                    new_box.add_item(item_to_move)
                    item_list.remove(item_to_move)
            box_list.append(new_box)
        output = box_list.copy()
    #print(output)
    return output


def main_menu():
    prompt = ('Please select an action:\n\n' +
        '(1) Create New Box\n' +
        '(2) Manage Existing Box\n' +
        '(3) Manage Unboxed Items\n' +
        '(4) Get Moving Documents\n' + 
        "(5) It's A Secret to Everybody...\n" + 
        '(6) Quit\n\n>>>')
    menu_choice = input(prompt)
    while menu_choice not in ('1', '2', '3', '4', '5','6'):
            print('\nYou must select a valid action!\n')
            menu_choice = input(prompt)
    return menu_choice


def item_new_name():
    new_item_name = input('Enter the item name:\n>>>')
    while len(new_item_name) == 0:
        print('Item name must not be empty.\n\n')
        new_item_name = input('Enter the item name:\n>>>')
    return new_item_name


def item_new_value():
    value_correct = False
    while not value_correct:
        try:
            new_item_value = float(input("\nEnter the item's value " +
            "(numbers only):\n>>>"))
            while new_item_value < 0:
                print('\nValue must be at least 0!\n')
                new_item_value = float(input("Enter the item's value " +
            "(numbers only):\n>>>"))
            value_correct = True
        except ValueError:
            print('\nValue must be a number!\n')
    return new_item_value


def item_new_quantity():
    quantity_correct = False
    while not quantity_correct:
        try:
            new_item_quantity = int(input("\nEnter the item's quantity:\n>>>"))
            while new_item_quantity < 1:
                print('\nQuantity must be at least 1!\n')
                new_item_quantity = int(input("Enter the item's quantity:" +
                "\n>>>"))
            quantity_correct = True
        except ValueError:
            print('\nQuantity must be an integer!\n')
    return new_item_quantity


def item_new_serial():
    serial_exists = input('\nDoes the item have a serial number? (Y/N)\n>>>')
    while serial_exists.lower() != 'y' and serial_exists.lower() != 'n':
        print('\nPlease enter Y or N.\n')
        serial_exists = input('Does the item have a serial number? (Y/N)\n>>>')
    if serial_exists.lower() == 'y':
        new_item_serial = input('\nPlease enter the serial number:\n>>>')
    else:
        new_item_serial = ''
    return new_item_serial


def item_new_picture(item_name):
    item_picture_choice = input('\nDo you have a picture for this item? (Y/N)' +
        '\n>>>')
    while (item_picture_choice.lower() != 'y'
        and item_picture_choice != 'n'):
        print('\nPlease select Y or N.\n')
        item_picture_choice = input('Do you have a picture for this item?' +
            '(Y/N)\n>>>')
    if item_picture_choice.lower() == 'y':
        item_picture_exists = False
        while not item_picture_exists:
            try:
                new_item_picture = input('\nPlease enter the picture file ' +
                'location:\n>>>')
                picture_file = Image.open(new_item_picture)
                picture_file.show()
                correct_picture = input('\nIs this the correct picture? ' +
                    '(Y/N)\n>>>')
                while (correct_picture.lower() != 'y' 
                    and correct_picture.lower() != 'n'):
                    print('\nPlease enter Y or N.\n')
                    correct_picture = input('Is this the correct picture? ' +
                        '(Y/N)\n>>>')
                if correct_picture == 'y':
                    picture_filename = str(int.from_bytes(
                        item_name.encode(), 'little')) + '.png'
                    try:
                        picture_file.save(picture_filename)
                        picture_file.close()
                        item_picture_exists = True
                    except OSError:
                        print('\nSomething went wrong while saving ' +
                            'the picture.\n')
            except FileNotFoundError:
                print('\nPlease enter a valid file location.\n')
            except OSError:
                print('\nPlease enter a valid file location.\n')
            except PIL.UnidentifiedImageError:
                print('\nImage cannot be identified.\n')
            
    else:
        picture_filename = ''
    return picture_filename


def create_item(item_box_number=0) -> Item:
    new_item_name = item_new_name()
    new_item_value = item_new_value()
    new_item_quantity = item_new_quantity()
    new_item_serial = item_new_serial()
    new_item_picture = item_new_picture(new_item_name)
    new_item_box = item_box_number
    new_item = Item(new_item_name, value=new_item_value, 
        quantity=new_item_quantity, serial=new_item_serial, 
        picture=new_item_picture, box=new_item_box)
    return new_item


def create_box(box_list, box_number):
    new_box_room = input('\nPlease enter the room for this box:' +
        '\n>>>')
    while len(new_box_room) == 0:
        new_box_room = input('Please enter a room. ' +
        'Enter the room for this box:\n>>>')
    new_box = Box(box_number, new_box_room)
    box_list.append(new_box)
        

def create_box_menu(create_box_list):
    keep_going = True
    while keep_going:
        # Print box numbers
        print('Boxes:\n')
        box_number_list = []
        for box in create_box_list:
            box_number_list.append(box.get_number())
        box_number_list.sort()
        if len(box_number_list) != 0:
            for num in box_number_list:
                print('Box ' + str(num) + '\n')
            next_box = str(box_number_list[-1] + 1)
        else:
            print('No Boxes\n')
            next_box = '1'
        
        # Prompt to start next box
        choice = input('Start Box ' + next_box + '? (Y/N)'+
            '\n>>>')
        while choice.lower() != 'y' and choice.lower() != 'n':
            print('\nYou must select Y or N.\n')
            choice = input('Start Box ' + next_box + 
                '? (Y/N)\n>>>')
        
        if choice.lower() == 'y':
            create_box(create_box_list, int(next_box))
            item_choice = input('\nAdd item to box? (Y/N)\n>>>')
            while item_choice.lower() != 'y' and item_choice.lower() != 'n':
                print('\nYou must select Y or N.\n')
                item_choice = input('\nAdd item to box? (Y/N)\n>>>')
            if item_choice.lower() == 'y':
                add_items = True
                while add_items:
                    print()
                    for boxes in create_box_list:
                        if int(next_box) == boxes.get_number():
                            boxes.add_item(create_item(boxes.get_number()))
                    add_more_items = input('\nAdd another item? (Y/N)' +
                        '\n>>>')
                    while (add_more_items.lower() != 'y' 
                        and add_more_items.lower() != 'n'):
                        print('\nPlease enter Y or N.\n')
                        add_more_items = input('Add another item? (Y/N)' +
                            '\n>>>')
                    if add_more_items.lower() == 'n':
                        add_items = False
        for boxes in create_box_list:
            for item in boxes.get_items():
                if item.get_box() != boxes.get_number():
                    boxes.remove_item(item)
        else:
            keep_going = False


def view_item(item_object):
    print(item_object)
    if item_object.get_picture() != '':
        pic = Image.open(item_object.get_picture())
        pic.show()
        pic.close()


def item_view_menu(view_boxes):
    view_item_choice = input('\nDo you want to view an item? (Y/N)\n>>>')
    while view_item_choice.lower() not in ('y', 'n'):
        print('\nPlease enter Y or N.\n')
        view_item_choice = input('Do you want to view an item? ' +
        '(Y/N)\n>>>')
    if view_item_choice.lower() == 'y':
        keep_viewing = True
        while keep_viewing:
            view_item_name = input('Enter the item to view:\n>>>')
            for view_box in view_boxes:
                for item_view in view_box.get_items():
                    if view_item_name.lower() in item_view.get_name():
                        view_item(item_view)
            keep_viewing_choice = input('\nView more items? (Y/N)\n>>>')
            while keep_viewing_choice.lower() not in ('y', 'n'):
                print('Please enter Y or N.\n')
                keep_viewing_choice = input('\nView more items? (Y/N)' +
                    '\n>>>')
            if keep_viewing_choice.lower() == 'y':
                for view_box in view_boxes:
                    print()
                    print(view_box)
            else:
                keep_viewing = False


def manage_item(item_list, item_object, box_set):
    keep_managing = True
    while keep_managing:
        print(item_object, '\n')
        menu_prompt = ('Please select an item option:\n' +
            '(1) Change Item Name\n' +
            '(2) Change Item Value\n' +
            '(3) Change Item Quantity\n' +
            '(4) Change Item Serial #\n' +
            '(5) Change Item Picture\n' +
            '(6) Change Item Box\n' +
            '(7) Delete Item\n' +
            '(8) Return to Previous Menu\n\n>>>'
        )
        choice = input(menu_prompt)
        while choice not in ('1', '2', '3', '4', '5', '6', '7', '8'):
            print('\nPlease select a valid option.\n')
            choice = input(menu_prompt)
        if choice == '7':
            delete_choice = input('Are you sure you want to delete this item?' +
                '(Y/N)\n>>>')
            while delete_choice.lower() not in ('y', 'n'):
                print('\nYou must enter Y or N.\n')
                delete_choice = input('Are you sure you want to delete this item?' +
                '(Y/N)\n>>>')
            if delete_choice.lower() == 'y':
                item_list.remove(item_object)
                print(item_list)
                keep_managing = False
        else:
            if choice == '1':
                item_object.update_name(item_new_name())
            elif choice == '2':
                item_object.update_value(item_new_value())
            elif choice == '3':
                item_object.update_quantity(item_new_quantity())
            elif choice == '4':
                item_object.update_serial(item_new_serial())
            elif choice == '5':
                item_object.update_picture(item_new_picture(item_object.get_name()))
            elif choice == '6':
                valid_entry = False
                while not valid_entry:
                    try:
                        new_item_box = int(input('Enter a new box #:\n>>>'))
                        while new_item_box not in box_set:
                            print('\nYou must choose an existing box.\n')
                            new_item_box = int(input('Enter a new box #:\n>>>'))
                        item_object.update_box(new_item_box)
                        valid_entry = True
                    except ValueError:
                        print('\nYou must enter an existing box #.\n')
            keep_going_choice = input('Keep managing item? (Y/N)\n>>>')
            while keep_going_choice.lower() not in ('y', 'n'):
                    print('\nYou must enter Y or N.\n')
                    keep_going_choice = input('Keep managing item? (Y/N)\n>>>')
            if keep_going_choice.lower() == 'n':
                keep_managing = False
# Missing features:
# ---If box # is changed, remove item from items list and add to the appropriate
#    box.
# ---If item name is changed, rename picture file according to new item name.
# ---If item name is changed, check it against other items to make sure another
#    item does not have the same name.  


def manage_boxes_menu():
    choice = input('Select an option:\n\n' +
        '(1) View Boxes\n' +
        '(2) Search Boxes\n' +
        '(3) Edit Boxes\n' +
        '(4) Exit to Main Menu\n\n>>>')
    while choice not in ('1', '2', '3', '4'):
        print('\nPlease enter a valid choice.\n')
        choice = input('Select an option:\n\n' +
        '(1) View Boxes\n' +
        '(2) Search Boxes\n' +
        '(3) Edit Boxes\n' +
        '(4) Exit to Main Menu\n\n>>>')
    return choice
    

def view_boxes(view_boxes_list):  # Need to implement add_item
    keep_going = True
    while keep_going:
        print('Boxes:\n')
        box_number_list = []
        for box in view_boxes_list:
            box_number_list.append(str(box.get_number()))
        box_number_list.sort()
        if len(box_number_list) != 0:
            for num in box_number_list:
                print('Box ' + str(num) + '\n')
            to_view = input('Enter a box # to view its contents:\n>>>')
            while to_view not in box_number_list:
                print('\nPlease select a valid box number\n')
                to_view = input('Enter a box # to view its contents:\n>>>')
            for view_box in view_boxes_list:
                if str(view_box.get_number()) == to_view:
                    print()
                    print(view_box)
                    break
            item_view_menu(view_boxes_list)
        else:
            print('No Boxes\n')
        go_again = input('View another box? (Y/N)\n>>>')
        while go_again.lower() not in ('y', 'n'):
            print('Please select Y or N.\n')
            go_again = input('View another box? (Y/N)\n>>>')
        if go_again.lower() == 'n':
            keep_going = False


def box_search(search_boxes_list):
    keep_going = True
    box_room_set = set()
    for search_box in search_boxes_list:
        box_room_set.add(search_box.get_room())
    box_item_set = set()
    for search_box in search_boxes_list:
        for search_item in search_box.get_items():
            box_item_set.add(search_item.get_name())        
    while keep_going:
        choice = input('Please select a search option:\n\n' +
            '(1) Search by Room\n' +
            '(2) Search by Item\n' +
            '(3) Exit\n\n>>>')
        while choice not in ('1', '2', '3'):
            print('\nPlease select a valid opton.\n')
            choice = input('Please select a search option:\n\n' +
                '(1) Search by Room\n' +
                '(2) Search by Item\n' +
                '(3) Exit\n\n>>>')
        if choice == '1':
            room_to_search = input('Enter the box room:\n>>>')
            if room_to_search.lower() not in box_room_set:
                print('\nThere are no boxes for that room.\n')
            else:
                for search_box in search_boxes_list:
                    if search_box.get_room() == room_to_search.lower():
                        print()
                        print(search_box)
                        item_view_menu(search_box)
        elif choice == '2':
            item_to_search = input('Enter the item to find:\n>>>')
            search_item_exists = False
            for search_item_name in box_item_set:
                if item_to_search.lower() in search_item_name:
                    search_item_exists =True
            if search_item_exists:
                view_item_boxes = []
                for search_box in search_boxes_list:
                    for search_item in search_box.get_items():
                        if item_to_search.lower() in search_item.get_name():
                            view_item_boxes.append(search_box)
                            print()
                            print(search_box)
                            print()
                item_view_menu(view_item_boxes)
            else:
                print('\nItem does not exist.\n')
        else:
            keep_going = False


def manage_boxes(manage_box_list):
    choice = '0'
    while choice != '4':
        choice = manage_boxes_menu()
        if choice == '1':
            print()
            view_boxes(manage_box_list)
            print()
        elif choice == '2':
            print()
            box_search(manage_box_list)
            print()
        elif choice == '3':
            edit_boxes(manage_box_list)


def manage_unboxed_items(item_list, box_list):
    if len(item_list) == 0:
        print('\nThere are no unboxed items.\n')
        time.sleep(0.5)
    else:
        box_number_set = set()
        for boxx in box_list:
            box_number_set.add(boxx.get_number())
        manage_item_menu(item_list, box_number_set)


def manage_item_menu(item_list, box_set):
    item_set = set()
    for list_item in item_list:
            item_set.add(list_item.get_name())
    print('Items:\n')
    for list_item in item_list:
        print(list_item, '\n')
    item_to_manage = input('Enter an item to manage:\n>>>')
    search_item_exists = False
    for search_item_name in item_set:
        if item_to_manage.lower() in search_item_name:
            search_item_exists =True
    if search_item_exists:
        for list_item in item_list:
            if item_to_manage.lower() in list_item.get_name():
                manage_item(item_list, list_item, box_set)
    else:
        print('\nItem does not exist.\n')


def moving_document_menu(box_list):
    box_number_set = set()
    keep_printing = True
    while keep_printing:
        if len(box_list) > 0:
            print('Boxes:\n')
            for moving_box in box_list:
                print('Box', moving_box.get_number())
                box_number_set.add(str(moving_box.get_number()))
            box_choice = input('Please select a box #:\n>>>')
            while box_choice not in box_number_set:
                print('\nPlease select a valid box #:\n')
                box_choice = input('Please select a box #:\n>>>')
            for moving_box in box_list:
                if box_choice == str(moving_box.get_number()):
                    chosen_box = moving_box
            qr_choice = input('Print QR code for box #' + box_choice + '? (Y/N)\n>>>')
            while qr_choice.lower() not in ('y', 'n'):
                print('\nPlease enter Y or N.\n')
                qr_choice = input('Print QR code for box #' + box_choice + '? (Y/N)\n>>>')
            if qr_choice.lower() == 'y':
                box_qr = qrcode.make(str(chosen_box))
                box_qr.show()
                box_qr.close()
                keep_going_choice = input('\nPrint another code? (Y/N)\n>>>')
                while keep_going_choice.lower() not in ('y','n'):
                    print('\nPlease enter Y or N.\n')
                    keep_going_choice = input('\nPrint another code? (Y/N)\n>>>')
                if keep_going_choice.lower() == 'n':
                    keep_printing = False
                    break  # Need to fix boolean to get rid of break
            elif qr_choice.lower() == 'n':
                keep_printing = False
        else:
            print('\nNo boxes found.\n')
            keep_printing = False


def secret():
    webbrowser.open('https://vlipsy.com/vlip/MzCA8MQv')


def program_quit():
    return None


def main():
    print('Welcome to Move Helpr!\n')
    user = input('Enter your username: >>>')
    user_directory = login(user)
    items_exist = check_user_dir(user, user_directory)
    user_item_file = get_item_file(user, user_directory, items_exist)
    user_items = get_items(user_item_file)
    user_boxes = get_boxes(user_items)
    print('\nWelcome to Move Helpr!')
    choice = main_menu()
    while choice != '6':
        if choice == '1':
            print()
            create_box_menu(user_boxes)
            print()
            choice = main_menu()
        elif choice == '2':
            print()
            manage_boxes(user_boxes)
            print()
            choice = main_menu()
        elif choice == '3':
            print()
            manage_unboxed_items(user_items, user_boxes)
            print()
            choice = main_menu()
        elif choice == '4':
            print()
            moving_document_menu(user_boxes)
            print()
            print(str(user_items))
            choice = main_menu()
        elif choice == '5':
            secret()
            print()
            choice = main_menu()
    program_quit()
    print('Thanks for using Move Helpr!')
    time.sleep(1)


main()
