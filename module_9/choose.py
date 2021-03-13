# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 9 Practice 10
#
# Returns number of ways to choose k elements from n choices
# -----------------------------------------------------------------------------

def choices(k, n):
    
    if k == 0 or k == n:
        return 1
    else:
        return choices(k-1, n-1) + choices(k, n-1)

print(choices(2, 3))