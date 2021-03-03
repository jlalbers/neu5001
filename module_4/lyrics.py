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

    animal = str(animal)
    sound = str(sound)
    
    verse = ('Old MacDonald had a farm, ee-igh, ee-igh, oh!\n'
             + 'And on that farm he had a ' + animal + ', ee-igh, ee-igh, oh!\n'
             + 'With a ' + sound + ', ' + sound + ' here and a ' + sound
             + ', ' + sound + ' there.\n'
             + 'Here a ' + sound + ', there ' + sound + ', everywhere a '
             + sound + ', ' + sound + '.\n'
             + 'Old MacDonald had a farm, ee-igh, ee-igh, oh!\n')

    return verse

def main():

    test_list = [('cow', 'moo'), ('sheep', 'baaa'), ('pig', 'oink'), (1, 4.0), ((1, 2), ['hi', 'there'])]
    
    for item in test_list:
        (x, y) = item
        verse = make_verse(x, y)


main()
