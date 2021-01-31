'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 4

Adds two numbers and returns the sum.
'''


def plus(x, y):
    '''Function: plus\n
       Parameters: two numbers\n
       Returns: sum of the numbers'''
    
    return x + y


def main():

    first = float(input('Enter the first number: '))
    second = float(input('Enter the second number: '))

    sum = plus(first, second)
    print(sum)


main()
