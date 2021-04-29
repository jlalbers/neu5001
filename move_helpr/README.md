# **Move Helpr Documentation** <!-- omit in toc -->
### **Current Version: v0.1** <!-- omit in toc -->

Move Helpr is a prototype application designed to make your move easier. This project originated as my final project for Northeastern University - Vancouver's CS 5001 final project assignment.

---

## **Table of Contents** <!-- omit in toc -->
- [**Download and Use**](#download-and-use)
  - [**Download Instructions**](#download-instructions)
  - [**Running the Program**](#running-the-program)
- [**Features**](#features)
  - [**Items**](#items)
  - [**Boxes**](#boxes)
  - [**Actions**](#actions)
- [**Known Issues and Bugs**](#known-issues-and-bugs)
- [**Planned Features**](#planned-features)
- [**Changelog**](#changelog)
  - [**v0.x**](#v0x)
- [**Source Code Documentation**](#source-code-documentation)
  - [**Class `item`**](#class-item)
    - [**Constructor**](#constructor)
    - [**Attributes**](#attributes)
    - [**Methods**](#methods)
  - [**Class `box`**](#class-box)
    - [**Constructor**](#constructor-1)
    - [**Attributes**](#attributes-1)
    - [**Methods**](#methods-1)
  - [**Functions**](#functions)

---

## **Download and Use**

Refer to these instructions to properly download and use the program. The program requires the installation of Python 3 and the following external Python packages to function:

* qrcode
* reportlab
* PIL (installed with qrcode)

### **Download Instructions**

To download the program, simply save the *driver, item,* and *box* Python files to the same directory. It is recommended to save them to C:\Users\ < username > \MoveHelpr to ensure access to PATH variables.

### **Running the Program**

To start the program, simply run the *driver* file. You will be prompted to enter a username to create a profile; enter your preferred username and the program will create a new user folder in the MoveHelpr directory. This user directory will store your item file as well as any item pictures that you associate with an item. Please do not delete these fles unless you want all your info to be deleted!

---

## **Features**
Move Helpr helps you keep track of your items and boxes while you're moving. Accordingly, the program revolves around the creation and management of Item objects and Box objects. For specific implementation of the item and box classes see [Source Code Documentation](#source-code-documentation).

### **Items**
Item objects store all the information for unique items. You can store the following item information:
 1. **Name**  
   The unique name of the item. To create a new item, you MUST give the item a unique name. When choosing an item name, it's best to be as descriptive as possible: for example, instead of naming something "shirt", you should use a more descriptive name like "Old Navy Flannel Gingham Blue Green Button Up Shirt". This will also help when searching for items: you can simply enter the search term "shirt" and all items with "shirt" in their name will be shown.

2. **Value**  
   (Optional) The value of a single item. The value must be at least 0.00. The value is not
   associated with a particular currency; currency support and conversion is
   planned to be supported in a future release. Additionally, the value is for
   each indidvidual item: if the item quantity is more than 1, just enter the
   value for a single item.

3. **Quantity**  
   (Optional) The quantity of the unique item. For example, if you are entering silverware, you could have the item "Dinner Fork" assigned a quantity of 8 if you have 8 forks.

4. **Serial**  
   (Optional) The item's serial number. This item attribute is optional, as not every item is serialized. However, it can help you keep track of serialized or high-value items to ensure that they weren't damaged and replaced or switched in transit.

5. **Picture**  
   (Optional) A picture of the item. It's stored as the path to the picture file in the user's folder. Pictures can be used to help identify items during unpacking or support a damaged goods claim.

6. **Box**  
   (Optional) The number of the box in which the item is stored. If the item is not in a box, it's box number will be listed as 0.

### **Boxes**
Box objects contain and organise items. They also aggregate the value of all the items they contain. Boxes contain the following information:

1. **Number**  
   The number of the box. It is used to select and identify different boxes, as well as associate items with a particular box. Box numbers are always a natural number.

2. **Room**  
   (Optional) The room where the box was packed and should be unpacked. This helps to group like items together: for example, a box from the kitchen would contain items like silverware, small appliances, etc. while a bedroom box might contain clothing, sheets, clocks, etc. If no room is entered, it will default to "Room TBD".

3. **Items**  
   (Optional) A list of the items stored in the box. Each item must be an Item object. Items can be added and removed from the box. The list can also be empty if the box does not currently have any items in it.

4. **Value**  
   The total value of all the items in the box. It is calculated automatically from the values of the box's items.

### **Actions**
The program allows for several actions to enable the creation and management of your moving inventory. For more details about specific implementations, consult the [Source Code Documentation.](#source-code-documentation)

1. **Creation**  
   You can create new items and boxes from within the program. When creating an item, you must enter the required parameters. See the documentation for default values.

2. **Editing**  
   Item and box attributes can be edited from the user menu. This can be used to correct mistakes or add additional description for an item after it has already been created.

3. **Deletion**  
   Items and boxes can be deleted. Be aware that once something is deleted, it's gone for good!

4. **Search**  
   Search for items by box room or by the item name. Keywords are allowed: i.e. searching for "bedroom" will return all items in a box where "bedroom" is in the box room, searching for the item "shirt" will return all items that have "shirt" in the item name, etc.

5. **Create Documents**  
   The program can generate documents from your items and boxes, such as inventory sheets for an individual box or a master list of all items for your move. QR codes can also be generated to tape/print onto boxes that contain the box information and item list. Currently, only QR codes are implemented, but a full document suite is planned for a future release.

---
## **Known Issues and Bugs**
1. **Item Importation** - If more than one item is stored in the items .csv file, only the first item will be automatically added to the box. The rest will be added to the unboxed items list despite having an assigned box.
   
2. **Box Creation** - New boxes will copy all items from all other boxes to their item list. Likewise, trying to remove an item from a box will remove it from all boxes.
   
3. **Edit Boxes** - This feature is unimplemented due to the box creation bug.

4. **Change Item Name** - Changing the item name will not change the filename of the picture. However, the filepath will be the same and the picture will still open.

5. **Delete Item** - Deleting an item will not delete the associated picture.

6. **Saving Information** - Exiting the program will not save any changes made to the item .csv file. This will be implemented after fixing other bugs.

---
## **Planned Features**
* **Currency Settings/Conversion**  
  Set values in a particular currency or switch between currencies for international moves.

* **Moving Documents**  
  Generate inventory sheets on a box or move scale. Integrate other applications such as DocuSign to generate boilerplate forms and agreements for moving/transportation companies.

* **Different User Types**  
  Add a user type for moving/transportation companies to allow them to upload custom forms, track multiple client moves, and keep a master list of schedules.

* **Cloud Storage**  
  Store user's data in a cloud location to enable access from any device, any location.

* **Hybrid Application Front-End**  
  GUI-based interface running as a web application as well as inside a native application wrapper for mobile devices.

---
## **Changelog**

### **v0.x**  
* **v0.1** - Initial upload and documentation.

---
## **Source Code Documentation**
### **Class `item`**
#### **Constructor**  

`Item(name, value=0.0, quantity=1, serial='', picture='', box=0)`: `Item` object constructor method
* Parameters:  
  `name`: accepts `str` argument. Returns `TypeError` if argument is not a `str` or `ValueError` if empty string is passed.

  `value`: accepts `int` or `float` argument. Passes `0.0` if no argument is given. Returns `TypeError` if argument is not a `str` or `float` or `ValueError` if the value passed is less than `0`.

  `quantity`: accepts `int` argument. Passes `1` if no argument is given. Returns `TypeError` if argument is not an `int` or `ValueError` if argument is less than `1`.

  `serial`: accepts `str` argument. Passes empty `str` if no argument is given. Returns `TypeError` if argument is not `str`.

  `picture`: accepts `str` argument. Passes empty `str` if no argument is given. Returns `TypeError` if argument is not `str`.

  `box`: accepts `int` argument. Passes `0` if no argument is given. Returns `TypeError` if argument is not `int` or `ValueError` if argument is less than `0`.

* Outputs:
  `Item` object

#### **Attributes**

`self.name`: item name. Type `str`

`self.id`: item ID. Type `int`. Generated with `name` parameter from constructor method using `int.from_bytes(name.encode(), 'little')`

`self.value`: item value. Type `float`

`self.quantity`: item quantity. Type `int`

`self.serial`: item serial number. Type `str`

`self.picture`: item picture file path. Type `str`

`self.box`: item box. Type `int`

#### **Methods**

`get_name()`: name getter method
* Parameters: None
* Outputs:  
  `self.name`

`get_id()`: ID number getter method
* Parameters: None
* Outputs:  
  `self.id`

`get_value()`: value getter method
* Parameters: None
* Outputs:  
  `self.value`

`get_quantity()`: quantity getter method
* Parameters: None
* Outputs:  
  `self.quantity`

`get_serial()`: serial number getter method
* Parameters: None
* Outputs:  
  `self.serial`

`get_picture()`: picture filepath getter method
* Parameters: None
* Outputs:  
  `self.picture`

`get_box()`: box number getter method
* Parameters: None
* Outputs:  
  `self.box`

`update_name(new_name)`: number setter method
* Parameters:  
  `new_name`. Type `int`. Returns `TypeError` if argument not `int` or `ValueError` if argument is empty `str`. Also updates `self.id`
* Outputs: None

`update_value(new_value)`: value setter method
* Parameters:  
  `new_value`: Type `int` or `float`. Returns `TypeError` if argument not `int, float` or `ValueError` if argument is less than `0`
* Outputs: None

`update_quantity(new_quantity)`: quantity setter method
* Parameters:  
  `new_quantity`: Type `int`. Returns `TypeError` if argument is not `int` or `ValueError` if argument is less than `1`.
* Outputs: None

`update_serial(new_serial)`: serial number setter method
* Parameters:  
  `new_serial`: Type `str`. Returns `TypeError` if argument is not `str`
* Outputs: None

`update_picture(new_picture)`: picture filepath setter method
* Parameters:  
  `new_picture`: Type `str`. Returns `TypeError` if argument is not `str`

`update_box(new_box)`: box number setter method
* Parameters:  
  `new_box`: Type `int`. Returns `TypeError` if argument is not `int` or `ValueError` if argument is less than `0`
* Outputs: None

`__str__()`: object `str` getter method
* Parameters: None  
* Outputs:  
  `str` containing all item attributes

### **Class `box`**
#### **Constructor**

`Box(box_number, box_room, box_items = [])`: `Box` object constructor method
* Parameters:  
  `box_number`: Type `int`. Returns `TypeError` if argument is not `int` or `ValueError` if argument is less than `1`

  `box_room`: Type `str`. Returns `TypeError` if argument is not `str` or `ValueError` if argument is empty `str`

  `box_items`: Type `list`. Returns `TypeError` if argument is not `str` or if elements in list are not `Item` objects

#### **Attributes**

`self.box_number`: box number. Type `int`

`self.box_room`: box room. Type `str`

`self.box_items`: box items. Type `list`. Elements are `Item` objects.

`self.box_value`: box value. Type `float`. Assigned automatically based on `self.box_items`

#### **Methods**

`get_number()`: box number getter method
* Parameters: None
* Outputs:  
  `self.box_number`

`get_room()`: box room getter method
* Parameters: None
* Outputs:  
  `self.box_room`

`get_items()`: box items setter method
* Parameters: None
* Outputs:  
  `self.items`

`update_value()`: privete box value setter method
* Parameters: None
* Outputs: None  
  Private method to recalculate box value

`get_value()`: box value getter method
* Parameters: None
* Outputs:  
  `self.box_value

`add_item(new_item)`: box items setter method (adds `Item` to box)
* Parameters:  
  `new_item`: `Item` object. Raises `TypeError` if argument is not `Item` object
* Outputs: None

`remove_item(old_item)`: box items setter method (removes `Item` from box)
* Parameters:  
  `old_item`: `Item` object. Raises `TypeError` if argument is not `Item` object
* Outputs: None
  
`__str()__`: object `str` getter method
* Parameters: None
* Outputs:  
  `str` containing all box attributes

### **Functions**

---
```
                      |
                     _=_
                     \ /.           _=
        .-.    _ .-_ |  |_         |  |
 "   _  | |   | ||  \|    |_.--.   |  |
 |  | |_| |-__| ||          |  |,-.|  |-_   __
|H|-|   '                          |     | |  |
                                         |_|  |
Created in Vancouver :)
```