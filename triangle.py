'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 2

This program reads the base length and height of a triangle
in inches and returns the area in millimeters
'''


def main():

    # Input base width and height from user
    base = float(input('Enter the base width in inches: '))
    height = float(input('Enter the height in inches: '))

    # Calculate the area in mm^2
    area = 0.5 * base * height * (25.4 ** 2)

    # Print the area of the triangle
    print('The area is', area, 'square millimeters')


main()
