'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 5

Converts a tuple to a list in the same order.'''

def convert_tuple(tuple):
    '''Function: convert_tuple\n
       Parameters: tuple\n
       Outputs: list with items from tuple'''

    output = []

    for x in range(len(tuple)):
        output.append(tuple[x])

    return output


def main():

    print(convert_tuple((1, 2, 3)))


main()