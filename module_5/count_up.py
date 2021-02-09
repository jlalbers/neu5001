'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 1

Counts up from 1 to an inputted integer.'''

def count_up(number):
    '''Function: count_up\n
       Parameters: any positive integer\n
       Outputs: prints numbers 1 through number'''

    number = int(number)  #Converts number to integer

    if number < 1:  
        print('Try function again with a positive nonzero number.')
    else:
        i = 1  # Initialize loop variable
        while i <= number:  # Loops print for integers from 1 to number
            print(i)
            i += 1
        
    return  # Ends function


def main():

    user_input = input('Enter a positive nonzero number: ')
    count_up(user_input)


main()
