'''
Jameson Albers
CS 5001
Spring 2021
Module 2 Practice 4

This program prints the price per litre of a six pack of
12 oz cans and a 2 litre bottle.
'''


def main():

    # Get price per 6 pack and 2 litre from user
    price_6_pack = float(input('Price per six-pack: '))
    price_2_litre = float(input('Price per two-litre: '))

    # Calculate price per litre
    unit_price_6_pack = price_6_pack / (6 * 0.355)
    unit_price_2_litre = price_2_litre / 2

    # Print unit prices
    print('Six-pack price per litre:', round(unit_price_6_pack, 2))
    print('Two-litre price per litre:', round(unit_price_2_litre, 2))


main()
