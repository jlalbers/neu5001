'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 3

Reads an input from the user and responds if input is "Hi".
'''


def main():

    # Get input from user
    greeting = input('Say something...\n')

    if greeting == 'Hi':
        print('Hi, how are you?\nDone.')

    else:
        print('Done.')


main()
