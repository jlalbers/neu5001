# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 3
#
# Description
# -----------------------------------------------------------------------------

def upper_triangle(n):
    if n <= 3:
        print('***\n**\n*')
    else:
        print('*' * n)
        upper_triangle(n-1)

upper_triangle(5)