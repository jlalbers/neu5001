'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 5

Gets a number and displays if it's even/odd and
positive/negative.
'''


def main():

    # Get number from user
    number = float(input('Enter an integer: '))

    if number % 2 == 0:
        if number < 0:
            print('Even negative number.')
        else:
            print('Even positive number.')

    else:
        if number < 0:
            print('Odd negative number.')
        else:
            print('Odd positive number.')


main()
