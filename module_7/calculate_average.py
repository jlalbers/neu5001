'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 4

Returns the average of a list of numbers.'''

def calculate_average(numbers):

    average = 0

    for i in numbers:
        average += i

    if len(numbers) != 0:
        average /= len(numbers)

    return average


def main():

    print(calculate_average([5, 4, 7]))


main()