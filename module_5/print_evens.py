'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 3

Prints even numbers from 2 through 100.'''

def print_evens():
    '''Function: print_evens\n
       Parameters: none\n
       Outputs: prints even numbers from 2 through 100'''

    i = 2  # Initialize loop variable
    while i <= 100:  # Loops print() for 2 thru 100
        print(i, end=' ')  # Prints values of i on the same line
        i += 2  # Advances to next even number

    return


def main():

    print_evens()


main()
