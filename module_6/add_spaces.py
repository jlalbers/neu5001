'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 2

Adds specified number of spaces between letters in given string.'''

def add_spaces(word, spaces):
    '''Function: add_spaces\n
       Parameters: string, integer number of spaces desired\n
       Outputs: string with added spaces between characters'''

    output = ''
    word = str(word)
    for x in range(len(word)):
        output = output + word[x] + (' ' * spaces)

    return output


def main():

    print(add_spaces('turtle', 8))


main()