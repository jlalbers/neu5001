# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 6
#
# Squares each element of a list starting at the given index
# -----------------------------------------------------------------------------

def to_squares(lst, index):
    if index < len(lst):
        lst[index] **= 2
        return to_squares(lst, index + 1)
    else:
        return lst

print(to_squares([1, 2, 3, 4, 5], 1))