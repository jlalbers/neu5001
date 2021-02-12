'''
Team 00
Module 5 Team Question 2'''

def staircase(even):
    '''Function: staircase
       Parameters: an even positive nonzero integer
       Outputs: staircase of '*' with number of rows from parameter'''

    print('\n'*3)

    half_even = even / 2

    i = 1
    
    while i <= half_even:
        spaces = (even - (2 * i)) * ' '
        stars = '* ' * 2 * i
        print((spaces + stars + '\n') * 2, end= '')
        i += 1

    return


def main():

    user_input = int(input('Enter an even, positive nonzero number: '))

    while user_input % 2 != 0 or user_input < 2:
        user_input = int(input('Enter an even, positive nonzero number: '))
    
    staircase(user_input)


main()
