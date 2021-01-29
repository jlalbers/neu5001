'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 4

Gets a number and clamps it between 1 and 100.
'''

def main():

    # Get number from user
    number = float(input('Enter value: '))

    # Clamp between 1 and 100
    if number > 100:
        number = 100
        print('Too big. Clamping reqired\nValue is', number)
    
    elif number < 1:
        number = 1
        print('Too small. Clamping reqired\nValue is', number)
    
    else:
        print('Value is', number)


main()
