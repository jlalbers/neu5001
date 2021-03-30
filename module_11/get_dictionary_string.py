# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 4
#
# Returns pairs of a dictionary as a string with one pair per line.
# -----------------------------------------------------------------------------

def get_value_string(dictionary):
    string = ''
    for key,value in dictionary.items():
        string += str(key) + ' - ' + str(value) + '\n'

    return string

def main():

    print(get_value_string({'One': 1, 'Two': 2, 'Three': 3}))


main()