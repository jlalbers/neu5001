'''
Jameson Albers
CS 5001, Spring 2021
Module X Practice X

Counts the number of vowels in a given string.'''

def count_vowels(word):

    vowels = 0
    word = word.casefold()
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1

    return vowels


def main():

    print(count_vowels('At the copa, copa cabana'))


main()