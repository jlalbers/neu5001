'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 7

Inputs a specified number of integers and calculates the sum and mean.'''

def calculations():
    '''Function: calculations\n
       Parameters: none\n
       Outputs: prints sum and average of inputted numbers.'''

    total = 0  # Initializes the variable for the sum
    count = int(input('Enter the number of values to read: '))
    i = count

    while i > 0:
        user_input = float(input('Enter number: '))
        total += user_input
        i -= 1

    average = total / count

    print('The sum is', total, '\nThe average is', average)

    return


def main():

    calculations()


main()
