'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 6

Reads positive integers from the keyboard and prints them as a list.'''

def read_values():
    '''Function: read_values\n
       Parameters: none\n
       Outputs: prints a list of integers until non- positive value is entered'''

    integer = int(input('Enter a number: '))
    output = []

    while integer > 0:
        output.append(integer)
        integer = int(input('Enter a number: '))

    print(output)

    return


def main():

    read_values()


main()