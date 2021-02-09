'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 4

Reads and prints positive values, stops if negative value is entered.'''

def non_negatives():
    '''Function: non_negatives\n
       Parameters: none\n
       Outputs: Prints inputted non-negative numbers until negative is entered
       '''

    user_input = float(input('Enter a non-negative number: '))

    while user_input > 0:
        print(user_input)
        user_input = float(input('And another one: '))

    print('DJ Khaled!!!')

    return


def main():

    non_negatives()


main()
