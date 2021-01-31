'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 2

Receives 2 numbers and returns the larger number.
'''


def larger(first, second):
    '''Function: larger
       Parameters: two numbers
       Returns: larger number'''

    if first > second:
        return first
    else:
        return second


def main():

    number_one = float(input('Enter the first number: '))
    number_two = float(input('Enter the second number: '))

    result = larger(number_one, number_two)

    print(result)


main()
