'''
Team 00
Module 5 - Team Question 1'''

def stars(number):
    '''Function: stars
       Parameters: integer number of stars
       Outputs: prints 1, 2, ... number of "*"'''

    number = int(number)
    i = 1  # Initialize loop variable
    while i <= number:
        print('*' * i)
        i += 1

    return


def main():

    user_input = int(input('Enter a positive nonzero integer: '))

    while user_input < 1:
        user_input = int(input('Enter a positive nonzero integer: '))

    stars(user_input)


main()
