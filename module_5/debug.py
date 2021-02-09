'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 9

Code debugging exercise.'''

def main():
  hi = int(input("Enter larger: "))
  lo = hi
  while lo >= hi:
    lo = int(input("Enter smaller: "))
  
  while hi >= lo:
    print(hi)
    hi -= 1
 
 
main()