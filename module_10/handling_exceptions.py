# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 10 Practice 4
#
# Handles exceptions from a program that creates random errors.
# -----------------------------------------------------------------------------

import random
random.seed(0)

def generate_random_error():
    value = random.randint(0, 3)
    if value == 0:
        raise ZeroDivisionError(value)
    elif value == 1:
        raise TypeError(value)
    elif value == 2:
        raise ValueError(value)
    else:
        raise NameError(value)

def main():

    zero = 0
    types = 0
    value = 0
    name = 0

    for i in range(20):
        try:
            generate_random_error()
        except ZeroDivisionError:
            print('Error', i + 1, ': Zero Division Error raised.')
            zero += 1
        except TypeError:
            print('Error', i + 1, ': Type Error raised.')
            types += 1
        except ValueError:
            print('Error', i + 1, ': Value Error raised.')
            value += 1
        except NameError:
            print('Error', i + 1, ': Name Error raised.')
            name += 1

    print('\nZero Division Errors:', zero)
    print('Type Errors:', types)
    print('Value Errors:', value)
    print('Name Errors:', name)

main()