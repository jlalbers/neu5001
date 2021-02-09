'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 6

Gets an integer and asks user to input one of its multiples.'''

def multiples():
    '''Function: multiples
       Parameters: none
       Outputs: Prints integer and the entered multiple.'''

    user_integer = int(input('Enter a non-zero integer: '))

    while user_integer < 1:
        user_integer = int(input('That was zero or netagive. Try again: '))

    user_multiple = int(input('Now enter one of its multiples: '))

    while user_multiple % user_integer != 0 or user_multiple == 0:
        user_multiple = int(input('Not a multiple. Try again: '))

    print('Integer:', user_integer, '\nMultiple:', user_multiple)

    return


def main():

    multiples()


main()
