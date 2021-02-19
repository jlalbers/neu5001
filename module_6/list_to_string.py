'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 4

Returns a string from a list with each element on its own line.'''

def list_to_string(list):
    '''Function: list_to_string\n
       Parameters: list\n
       Outputs: string with each item on its own line'''

    output = ''

    for x in range(len(list)):
        output = output + str(list[x]) + '\n'

    return output


def main():

    print(list_to_string(['cat', 59, 'moose']))


main()