'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 10

Prints each word in a string on its own line.'''

def count_words(sentence):

    words = sentence.split()

    for i in range(len(words)):
        print(str(i) + '. ' + words[i])
    

def main():

    count_words('Jiminny crickets, Batman! The Batmobile lost a wheel and the Joker ran away!')


main()