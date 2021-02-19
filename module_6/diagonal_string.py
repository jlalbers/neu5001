'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 3

Returns a diagonal string.'''

def diagonal_string(string):
    '''Function: diagonal_string\n
       Parameters: string\n
       Outputs: string formatted diagonally'''

    output = ''

    for x in range(len(string)):
        output = output + (' ' * x) + string[x] + '\n'

    return output


def main():

    print(diagonal_string('northeastern'))


main()