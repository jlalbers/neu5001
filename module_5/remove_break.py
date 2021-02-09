'''
Jameson Albers
CS 5001, Spring 2021
Module 5 Practice 10

Remove the break statement in a provided loop.'''

def main():
  a = 0
  b = 1
  print("0\n1")
  c = 0
  while c < 1000:
    c = a + b
    print(c)
    a = b
    b = c
    
 
main()