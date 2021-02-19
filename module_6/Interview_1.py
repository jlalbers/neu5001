def place_numbers():

    # Get number of values
    values = int(input('Enter the desired number of values: '))

    inputs = []  # Initialize list of inputs
    characters = []  # Initialize list of characters
    positions = []  # Initialize list of positions

    # Add user inputs to lists
    for x in range(values):
        character, position = input('Enter "value, position": ').split(', ')
        characters.append(character)
        positions.append(int(position))

    checker = positions  # List to check positions
    checker.sort()  # Sorts checker list

    for i in range(1, checker[-1]):  # Checks natural number range of positions
        if checker[i-1] != i:  # If a position is absent:
            positions.append(i)  # Adds position to positions list
            characters.append('_')  # Adds '_' to character list
        
    n = 0  # Initialize index variable

    # Make list of inputs formatted 'position' + 'character'
    for j in positions:
        inputs.append(str(j) + characters[n])
        n += 1  # Advances variable for indexing

    inputs.sort()  # Sorts inputs by position

    output = ''  # Initialize list of outputs
    for y in inputs:
        output += y[1:]  # Slice off position, add to output string

    return output

def main():

    print(place_numbers())


main()
