'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 1

Counts down from an inputted integer to 1.'''

def count_down(number):
    '''Function: count_down\n
       Parameters: any positive integer\n
       Outputs: prints numbers from number to 1.'''

    number = int(number)  #Converts number to integer

    if number < 1:  
        print('Try function again with a positive nonzero number.')
    else:
        i = number  # Initialize loop variable
        while i >= 1:  # Loops print for integers from number to 1
            print(i)
            i -= 1
        
    return  # Ends function


def main():

    user_input = input('Enter a positive nonzero number: ')
    count_down(user_input)


main()
