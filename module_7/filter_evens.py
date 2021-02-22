'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 7

Returns a list of the even values of a given list.'''

def filter_evens(numbers):

    evens = []

    for i in numbers:
        if i % 2 == 0 and i != 0:
            evens.append(i)

    return evens


def main():

    print(filter_evens([-2, -1, 0, 1, 2, 3, 4]))


main()