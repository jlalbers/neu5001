# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 4
#
# Prints a lower left triangle of size n.
# -----------------------------------------------------------------------------

def lower_triangle(n):
    if n <= 3:
        print('*\n**\n***\n', end='')
    else:
        lower_triangle(n-1)
        print('*' * n + '\n', end='')

lower_triangle(20)