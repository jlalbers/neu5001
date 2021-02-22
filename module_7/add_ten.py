'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 6

Adds 10 to each element in a list.'''

def add_ten(numbers):

    for i in range(len(numbers)):
        numbers[i] += 10

    return numbers


def main():

    print(add_ten([1, 2, 3, 4, 5]))


main()