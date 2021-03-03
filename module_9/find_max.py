# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 7
#
# Finds max value in a list of integers
# -----------------------------------------------------------------------------

def max_value(lst, max_index, check_index):
    '''Function: max_value\n
    Parameters: list of values, current index of max, index to check\n
    Initialize function with max_index = 0, check_index = 1\n
    Outputs: maximum value in list of ints/floats'''

    if check_index < len(lst):
        if lst[max_index] > lst[check_index]:
            return max_value(lst, max_index, check_index + 1)
        else:
            return max_value(lst, max_index +1, check_index + 1)
    else:
        return lst[max_index]

print(max_value([1, 4, 5, 324, 34532, 54, 34], 0, 1))