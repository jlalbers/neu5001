'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 9

This program gets two times in 24-hr time and calculates the time difference.
'''


def main():

    # Input times
    first = int(input('Enter the first time: '))
    second = int(input('Enter the second time: '))

    # Convert times to minutes
    first_minutes = ((first // 100) * 60) + (first % 100)
    second_minutes = ((second // 100) * 60) + (second % 100)

    # Calculate difference
    difference = second_minutes - first_minutes

    # Calculate hours and minutes
    hours = difference // 60
    minutes = difference % 60

    # Print time difference
    print(hours, 'hours', minutes, 'minutes')


main()
