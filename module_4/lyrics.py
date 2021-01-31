'''
Jameson Albers
CS 5001, Spring 2021
Module 4 Practice 10

Prints verses of 'Old Macdonald' for different animals.
'''


def make_verse(animal, sound):
    '''Function: make_verse\n
       Parameters: strings of animal and sound\n
       Outputs: verse using animal and sound'''

    verse = ('Old MacDonald had a farm, ee-igh, ee-igh, oh!\n'
             + 'And on that farm he had a ' + animal + ', ee-igh, ee-igh, oh!\n'
             + 'With a ' + sound + ', ' + sound + ' here and a ' + sound
             + ', ' + sound + ' there.\n'
             + 'Here a ' + sound + ', there ' + sound + ', everywhere a '
             + sound + ', ' + sound + '.\n'
             + 'Old MacDonald had a farm, ee-igh, ee-igh, oh!\n')

    print(verse)

    return


def main():

    print('Old Macdonald for Cows, Sheep, Pigs, Chickens, and Foxes\n')

    make_verse('cow', 'moo')
    make_verse('sheep', 'baa')
    make_verse('pig', 'oink')
    make_verse('chicken', 'cluck')
    make_verse('fox', 'EEKEEKEEKEEEEKEKEKEK')


main()
