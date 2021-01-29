'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 6

Gets 3 integers and determines if they are in ascending/descending order.
'''


def main():

    # Input numbers from user
    inputs = input('Enter three numbers separated by spaces: ').split()

    # Convert to floats
    for i in range(len(inputs)):
        inputs[i] = float(inputs[i])

    # Determine if numbers are in order
    if inputs[0] <= inputs[1] <= inputs[2]:
        print(inputs, 'In order')
    elif inputs[0] >= inputs[1] >= inputs[2]:
        print(inputs, 'In order')
    else:
        print(inputs, 'Not in order')


main()
