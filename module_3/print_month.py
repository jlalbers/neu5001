'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 9

Gets a number from 1-12 and prints the corresponding month.
'''
import datetime


def main():

    # Input number of month
    month = int(input('Enter month: '))

    # Check for valid month
    if 1 <= month <= 12:
        # Converts month to datetime object
        month = datetime.datetime(1, month, 1)
        # Prints string formatted full month name
        print(month.strftime('%B'))
    else:
        print('Unknown')


main()
