# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 5
#
# Sums values in a list starting at at given index through last item
# -----------------------------------------------------------------------------

def sum_values(lst, index):
    if index < len(lst):
        return lst[index] + sum_values(lst, index + 1)
    else:
        return 0

print(sum_values([1, 2, 3, 4, 5], 1))