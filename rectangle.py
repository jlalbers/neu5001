'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 3

This program reads the lengths of a rectangle's sides
and prints the area, perimeter, and length of the diagonal.
'''


def main():

    # Input width and height from the user
    height = float(input('Enter height: '))
    width = float(input('Enter Width: '))

    # Calculate area, perimeter, and diagonal length
    area = height * width
    perimeter = 2 * (height + width)
    diagonal = (height ** 2 + width ** 2) ** 0.5

    # Print the area, height, and diagonal
    print('The area of the rectangle is', area)
    print('The perimeter of the rectangle is', perimeter)
    print('The diagonal length is', diagonal)


main()
