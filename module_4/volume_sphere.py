'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 5

Gets radius of a sphere and outputs the volume.
'''


def volume_sphere(radius):
    '''Function: volume_sphere\n
       Parameters: radius\n
       Returns: volume of corresponding sphere'''

    PI = 3.14159
    volume = (4/3) * PI * radius ** 3

    return volume


def main():

    radius = float(input('Enter radius of sphere: '))

    result = volume_sphere(radius)
    print(result)


main()
