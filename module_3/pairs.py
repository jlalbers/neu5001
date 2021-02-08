'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 7

Reads 4 integers and checks for two matching pairs.
'''


def main():

    # Input numbers from user
    inputs = input('Enter four integers separated by spaces: ').split()

    # Convert to ints
    for i in range(len(inputs)):
        inputs[i] = float(inputs[i])

    # Sort list of inputs
    inputs.sort()

    # Check for two pairs
    if inputs[0] == inputs[1] and inputs[2] == inputs[3]:
        print(inputs, 'Two Pairs')
    else:
        print(inputs, 'Not Two Pairs')


main()
