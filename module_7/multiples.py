'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 1

Prints multiples of 5 up to an entered integer.'''

def multiples(number):

    number = int(number)
    for i in range(5,(number + 1), 5):
        print(i)

    return


def main():

    multiples(25)


main()