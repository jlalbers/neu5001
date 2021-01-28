'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 1

Reads 2 values sequentially and determines if the 1st value is
larger than the 2nd.
'''


def main():

    # Get first and second values
    first = float(input('Enter the first number: '))
    second = float(input('Enter the second number: '))
    
    # See if first value is smaller/larger than second value
    if first < second:
        print('The first number is smaller.')
    elif first > second:
        print('The first number is larger.')
    else:
        print('The number are the same.')


main()
