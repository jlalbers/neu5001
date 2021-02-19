'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 1

Returns the letter of a given index in a given string.'''

def extract_letter(string, index):
    '''Function: extract_letter\n
       Parameters: string and integer index\n
       Outputs: character of inputted string of inputted index'''

    output = string[index]

    return output


def main():

    input_1 = input('Enter your string: ')
    input_2 = int(input('Enter your index: '))

    while input_2 < 0:
        input_2 = int(input('Enter your index: '))

    print(extract_letter(input_1, input_2))


main()