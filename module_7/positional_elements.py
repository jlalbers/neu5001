'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 9

Returns the number of elements that are equivalent to that element's index.'''

def positional_elements(elements):

    total = 0
    for i in range(len(elements)):
        if elements[i] == i:
            total += 1

    return total


def main():

    print(positional_elements([0, 1, 2, 3, 5, 5]))


main()