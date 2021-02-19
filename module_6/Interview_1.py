def place_numbers():

    # Get number of values
    values = int(input('Enter the desired number of values: '))

    inputs = []  # Initialize list of inputs

    # Add user inputs to list
    for x in range(values):
        character, position = input('Enter "value, position": ').split(', ')
        inputs.append(position + character) # Put position in front of character

    inputs.sort()  # Sorts inputs by position

    output = ''  # Initialize list of outputs
    for y in inputs:
        output += y[1:]  # Slice off position, add to output string

    return output

def main():

    print(place_numbers())


main()