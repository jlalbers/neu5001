'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 7

This program gets two x,y points and calculates the distance between them.
'''


def main():

    # Input x1, y1, x2, y2
    x1 = int(input('Enter x1: '))
    y1 = int(input('Enter y1: '))
    x2 = int(input('Enter x2: '))
    y2 = int(input('Enter y2: '))

    # Calculate distance
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Convert points to strings for output
    point1 = '(' + str(x1) + ',' + str(y1) + ')'
    point2 = '(' + str(x2) + ',' + str(y2) + ')'

    # Print output
    print('The distance between', point1, 'and', point2, 'is', distance)


main()
