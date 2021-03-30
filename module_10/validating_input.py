# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 10 Practice 2
#
# Returns an ordered pair with one positive and one negative integer.
# -----------------------------------------------------------------------------

def main():

    one = int(input('Enter value: '))
    while one == 0:
        print('Value should be either negative or positive.')
        one = int(input('Enter value: '))

    two = int(input('Enter value: '))
    
    if one > 0 and two >= 0:
        while two >= 0:
            print('Value should be negative.')
            two = int(input('Enter value: '))
    elif one < 0 and two <= 0:
        while two <= 0:
            print('Value should be positive.')
            two = int(input('Enter value: '))

    pair = (one, two)

    print('Pair: ', pair)

main()