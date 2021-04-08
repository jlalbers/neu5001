# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Class Dictionary: Text File Builder
#
# This program collects user inputs for a word, defenition, and keywords, then
# converts them into a standardized text file for use with the compiler.
# -----------------------------------------------------------------------------
def get_word():
    output = input('Enter the word/term to define:\n').lower()
    return output


def get_definition():
    output = input('Enter the definition for the word/term:\n')
    return output


def get_keywords():
    output = input('Enter keywords, separated by a comma:\n').lower()
    output = output.replace(' ', '')
    return output


def write_dictionary(file, wrd, defn, keywds):
    file.write(wrd + ':::' + defn + ':::' + keywds + '\n')


def main():
    name = input('Please enter your first name:\n')
    filename = 'spring2021_dictionary_' + name.lower()
    try:
        dict_file = open(filename, 'a')
        print('Welcome to the Dictionary Creator!\n')
        keep_going = True
        while keep_going == True:
            word = get_word()
            definition = get_definition()
            keywords = get_keywords()
            write_dictionary(dict_file, word, definition, keywords)
            choice = input("Word successfully added. Add another word? (Y/N)\n")
            if choice.upper() == 'N':
                keep_going = False
        dict_file.close()
        print('Thank you for using Dictionary Creator!')
    except PermissionError:
        print('You do not have permission to append', filename)
    except OSError:
        print('Something went wrong while opening', filename)


main()
