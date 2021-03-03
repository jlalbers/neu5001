'''
Jameson Albers
CS 5001, Spring 2021
Module 9 Practice 1

Recursive program based on given function.'''

def formula(n):
    if n <= 1:
        return 3
    else:
        return 2 * formula(n-1) + 5

print(formula(4))