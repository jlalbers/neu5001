# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Class Dictionary: Search
#
# This program uses search terms to print words and definitions.
# -----------------------------------------------------------------------------

import ast

def get_dictionary(filename):
    # Reads class dictionary from text file and returns dictionary object
    dictionary = open(filename)
    contents = dictionary.read()
    output = ast.literal_eval(contents)  # Parses string into dictionary object
    dictionary.close()
    return output


def word_search(word, dictionary):
    # Searches dictionary for an entered word
    if word in dictionary:
        key, value = word, dictionary[word][0]
        # Prints word and all definitions
        print('Defenitions for', key, ':')
        for definition in value:
            print(definition)
    print()


def letter_search(letter, dictionary):
    # Searches words alphabetically
    for key in dictionary:
        # Searches first letter of all keys
        if key[0] == letter:
            print(key)
    print()


def keyword_search(keyword, dictionary):
    # Searches keywords associated with entries
    keyword = keyword.replace(' ', '')  # Eliminates white space
    for key in dictionary:
        # Prints word if keyword is in list of keywords for entry
        if keyword in dictionary[key][1]:
            print(key)
    print()


def main():
    # Open class dictionary text file as a dictionary object
    class_dict = get_dictionary('class_dictionary.txt')
    print('Thank you for searching the class dictionary!\n')
    stop = False
    # Looping search menu
    while stop == False:
        choice = input('''Select an option:\n
        (w) Search for a word\n
        (l) Search words by first letter\n
        (k) Search words by keyword\n
        (q) Quit\n''')
        if choice.lower() == 'w':  # Search by word
            search = input('Enter the word to search:\n')
            print()
            word_search(search, class_dict)
            print()
        elif choice.lower() == 'l':  # Search by first letter
            search = input('Enter the letter to search:\n')
            print()
            letter_search(search, class_dict)
            second_search = input('Enter a word to see its definitions:\n')
            print()
            # Look up definition for a listed word
            word_search(second_search, class_dict)
        elif choice.lower() == 'k':  # Search by keyword
            search = input('Enter a keyword to search:\n')
            print()
            keyword_search(search, class_dict)
            second_search = input('Enter a word to see its definitions:\n')
            # Look up definition for a listed word
            word_search(second_search, class_dict)
        elif choice.lower() == 'q':  # Quit the program
            stop = True
        else:  # Invalid menu option
            print('Please select a valid option.\n')
    print('Bye!')


main()
