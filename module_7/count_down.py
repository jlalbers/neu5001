'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 2

Prints from 100 to 0 ('Blastoff!') in multiples of 5.'''

def count_down():

    for i in range(100, 0, -5):
        print(i)
    
    print('Blastoff!')


def main():

    count_down()


main()
