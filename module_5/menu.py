'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 8

Iterates a menu of string concatenation based on user input.'''

def menu():
    '''Function: menu\n
       Parameters: none\n
       Outputs: Result of menu selections as string'''

    options = ('0. Quit\n1. Add "O"\n2. Add "oo"\n3. Add "xXx")')
    print(options)

    choice = input('Option: ')
    result = ''

    while choice != '0':

        if choice == '1':
            result += 'O'
        elif choice == '2':
            result += 'oo'
        elif choice == '3':
            result += 'xXx'
        else:
            print('Invalid option.')

        print(options)
        choice = input('Option: ')

    print('Result:', result)


def main():

    menu()


main()
