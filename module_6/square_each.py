'''
Jameson Albers
CS 5001, Spring 2021
Module 6 Practice 7

Receives a list and squares each element.'''

def square_each(items):

    for x in range(len(items)):
        items[x] **= 2

    return items


def main():

    print(square_each([1, 2, 3, 4, 5]))


main()
