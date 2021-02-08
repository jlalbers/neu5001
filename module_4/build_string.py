'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 9

Repeats a string over 3 lines a specified number of times.
'''


def build_string(string, first_line, second_line, third_line):
    '''Function: build_string\n
       Parameters: string and multiplier for each line\n
       Output: three lines of string'''

    build = (string * first_line + '\n' + string * second_line + '\n'
             + string * third_line + '\n')

    return build


def main():
    user_input = input('Enter the string you want to repeat: ')
    print(build_string(user_input, 4, 2, 3))


main()
