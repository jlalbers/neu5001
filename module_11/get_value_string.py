# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 3
#
# Returns values of a dictionary as a string with one value per line.
# -----------------------------------------------------------------------------

def get_value_string(dictionary):
    string = ''
    for value in dictionary.values():
        string += str(value) + '\n'

    return string

def main():

    print(get_value_string({'One': 1, 'Two': 2, 'Three': 3}))


main()