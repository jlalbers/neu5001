'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 5

Returns the count of negative numbers in a list.'''

def count_negatives(numbers):
    
    negatives = 0

    for i in numbers:
        if i < 0:
            negatives += 1

    return negatives


def main():

    print(count_negatives([-2, -1, 0, 1, 2]))


main()