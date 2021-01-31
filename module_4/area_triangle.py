'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 6

Returns the area of a triangle given its three sides.
'''
import math


def area_trinagle(side_1, side_2, side_3):
    '''Formula: area_triangle\n
       Parameters: lengths of triangle's sides\n
       Returns: area'''

    s = (side_1 + side_2 + side_3) / 2

    area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))

    return area


def main():

    one = float(input('Side one: '))
    two = float(input('Side two: '))
    three = float(input('Side three: '))

    area = area_trinagle(one, two, three)
    print(area)


main()
