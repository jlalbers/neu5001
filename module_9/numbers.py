# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 9
#
# Takes integer and returns the digits as English words
# -----------------------------------------------------------------------------

def numbers(number):
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number = str(number)
    if len(number) > 1:
        return numbers(number[:(len(number) - 1)]) + ' ' + digits[int(number[-1])]
    else:
        return digits[int(number)]

print(numbers(77894203))