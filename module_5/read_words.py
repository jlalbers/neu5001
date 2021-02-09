'''
Jameson Albers
CS 5001, Spring 2021
Module 5, Practice 5

Reads words until 'stop' is entered, then prints the words.'''

def read_words():
    '''Function: read_words
       Parameters: none
       Outputs: Prints words entered'''

    words = []  # Initializes list of words
    user_input = input('Enter a word: ')  # Takes first user input

    while user_input.casefold() != 'stop':  # Stops loop if 'stop' is entered
        words.append(user_input)  # Appends word list with input if not 'stop'
        user_input = input('Enter another word: ')  # Gets another word

    for i in range(len(words)):  # Prints words in list
        print(str(words[i]), end=' ', flush=True)  # Prints words on same line

    return


def main():

    read_words()


main()
