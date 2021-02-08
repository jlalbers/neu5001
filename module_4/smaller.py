'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 3

Gets 2 integers and returns the smaller one.
'''


def smaller(first, second):
    '''Function: smaller\n
       Parameters: two integers\n
       Returns: larger integer\n'''

    if first < second:
        return first
    else:
        return second


def main():

    input_1 = float(input('Enter the first integer: '))
    input_2 = float(input('Enter the second integer: '))

    result = smaller(input_1, input_2)
    print(result)


main()
