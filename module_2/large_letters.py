'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 10

This program prints HELLO in large letters.
'''


def main():

    # Create letters
    letter_h = 'H   H\nH   H\nHHHHH\nH   H\nH   H\n'
    letter_e = 'EEEEE\nE    \nEEEEE\nE    \nEEEEE\n'
    letter_l = 'L    \nL    \nL    \nL    \nLLLLL\n'
    letter_o = ' OOO \nO   O\nO   O\nO   O\n OOO \n'

    # Print letters
    print(letter_h + '\n' + letter_e + '\n' + 2 * (letter_l + '\n') + letter_o + '\n')


main()
