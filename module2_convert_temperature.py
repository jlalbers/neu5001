'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 5

This program gets the temperature in Kelving and prints
the equivalent temperature in Celsius and Fahrenheit.
'''


def main():

    # Get Kelvin temperature from user
    kelvin = float(input('Enter temperature in Kelvin: '))

    # Calculate temperature in Celsius/Fahrenheit
    celsius = kelvin - 273.15
    fahrenheit = (kelvin - 273.15) * (9 / 5) + 32

    # Prints temperatures
    print('The temperature in Celsius is', celsius)
    print('The temperature in Fahrenheit is', fahrenheit)


main()
