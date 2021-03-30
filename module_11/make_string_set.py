# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 6
#
# Takes a comma-delineated string and returns a set.
# -----------------------------------------------------------------------------

def make_string_set(string):
    return set(string.split(','))

def main():

    print(make_string_set('Jeremy,Alex,Beth,Emily'))


main()