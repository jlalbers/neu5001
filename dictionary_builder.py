# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Class Dictionary: Text File Builder
#
# This program collects user inputs for a word, defenition, and keywords, then
# converts them into a standardized .csv file for use with the compiler.
# -----------------------------------------------------------------------------

import csv

def get_word():
    # Gets word from the user and returns it as a string
    output = input('Enter the word/term to define:\n').lower()
    return output


def get_definition():
    # Gets definition from the user and returns it as string
    output = input('Enter the definition for the word/term:\n')
    return output


def get_keywords():
    # Gets keywords from the user and returns it as CSV
    output = input('Enter keywords, separated by a comma:\n').lower()
    output = output.replace(' ', '')
    return output


def write_dictionary(file_writer, wrd, defn, keywds):
    # Writes the word/definition/keywords as a line in the .csv file
    file_writer.writerow([wrd,defn,keywds.replace(' ','')])


def main():
    # Get user's name
    name = input('Please enter your first name:\n')
    # Creates filename with format 'spring2021_dictionary_name.csv'
    filename = 'spring2021_dictionary_' + name.lower() + '.csv'
    try:
        # Creates file/opens for appending
        with open(filename, 'a', newline='') as dict_file:
            print('Welcome to the Dictionary Creator!\n')
            # Initialize loop variable
            keep_going = True
            # Create csv writer object
            dict_writer = csv.writer(dict_file, delimiter=',', quotechar='"', 
            quoting=csv.QUOTE_MINIMAL)
            # Looping menu to add words to the dictionary
            while keep_going == True:
                # Get word, definition, and keywords
                word = get_word()
                definition = get_definition()
                keywords = get_keywords()
                # Write to dictionary
                write_dictionary(dict_writer, word, definition, keywords)
                choice = input(
                    "Word successfully added. Add another word? (Y/N)\n")
                if choice.upper() == 'N':
                    keep_going = False
        print('Thank you for using Dictionary Creator!')
    except PermissionError:
        print('You do not have permission to append', filename)
    except OSError:
        print('Something went wrong while opening', filename)


main()
