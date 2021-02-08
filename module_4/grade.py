'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 7

Gets a numeric grade and outputs the corresponding letter grade.
'''


def grade(score):
    '''Function: grade\n
       Parameters: numeric grade\n
       Returns: letter grade as string'''

    if score <0:
        return 'Please enter a valid score.'
    elif score >= 93:
        return 'A'
    elif score >= 90:
        return 'A-'
    elif score >= 86:
        return 'B+'
    elif score >= 82:
        return 'B'
    elif score >= 77:
        return 'B-'
    elif score >= 73:
        return 'C+'
    elif score >= 69:
        return 'C'
    elif score >= 65:
        return 'C-'
    elif score >= 0:
        return 'F'


def main():

    score = float(input('Enter your numeric grade: '))

    letter = grade(score)
    print('You scored: ', letter)


main()
