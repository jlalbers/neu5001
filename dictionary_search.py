# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Class Dictionary: Search
#
# This program uses search terms to print words and definitions.
# -----------------------------------------------------------------------------
import ast

def get_dictionary(filename):
    dictionary = open(filename)
    contents = dictionary.read()
    output = ast.literal_eval(contents)
    return output


def word_search(word, dictionary):
    if word in dictionary:
        key, value = word, dictionary[word][0]
        print('Defenitions for', key, ':')
        for definition in value:
            print(definition)
    print()


def letter_search(letter, dictionary):
    for key in dictionary:
        if key[0] == letter:
            print(key)
    print()


def keyword_search(keyword, dictionary):
    keyword = keyword.replace(' ', '')
    for key in dictionary:
        if keyword in dictionary[key][1]:
            print(key)
    print()

def main():
    class_dict = get_dictionary('class_dictionary.txt')
    print('Thank you for searching the class dictionary!\n')
    stop = False
    while stop == False:
        choice = input('''Select an option:\n
        (w) Search for a word\n
        (l) Search words by first letter\n
        (k) Search words by keyword\n
        (q) Quit\n''')
        if choice.lower() == 'w':
            search = input('Enter the word to search:\n')
            print()
            word_search(search, class_dict)
            print()
        elif choice.lower() == 'l':
            search = input('Enter the letter to search:\n')
            print()
            letter_search(search, class_dict)
            second_search = input('Enter a word to see its definitions:\n')
            print()
            word_search(second_search, class_dict)
        elif choice.lower() == 'k':
            search = input('Enter a keyword to search:\n')
            print()
            keyword_search(search, class_dict)
            second_search = input('Enter a word to see its definitions:\n')
            word_search(second_search, class_dict)
        elif choice.lower() == 'q':
            stop = True
        else:
            print('Please select a valid option.\n')
    print('Bye!')

main()
