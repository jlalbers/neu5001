'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 6

This program reads a measurement in meters and outputs
the measurement in inches, feet, and miles.
'''


def main():

    # Input the measurement in meters
    meters = float(input('Enter length: '))

    # Covert to inches, feet, and miles
    inches = meters * 39.3701
    feet = inches / 12
    miles = feet / 5280

    # Print results
    print('The length in inches is', inches)
    print('The length in feet is', feet)
    print('The length in miles is', miles)


main()
