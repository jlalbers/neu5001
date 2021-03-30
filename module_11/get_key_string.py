# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 2
#
# Returns keys of a dictionary as a string with one key per line.
# -----------------------------------------------------------------------------

def get_key_string(dictionary):
    string = ''
    for key in dictionary:
        string += str(key) + '\n'

    return string

def main():

    print(get_key_string({'One': 1, 'Two': 2, 'Three': 3}))


main()