'''
Jameson Albers
CS 5001, Spring 2021
Module 3 Practice 8

This program outputs a truth table based on inputted values and
predetermined comparisons.
'''


def main():
    # Make list of truth values
    p_values = [False, False, False, False, True, True, True, True]
    q_values = [False, False, True, True, False, False, True, True]
    r_values = [False, True, False, True, False, True, False, True]

    # Calculate A and B
    a_values = []
    b_values = []
    for i in range(8):
        a_values.append((p_values[i] and q_values[i]) or not r_values[i])
        b_values.append(not(p_values[i] and (q_values[i] or not r_values[i])))

    # Change True and False to T and F, format for table
    for i in range(8):
        p_values[i] = '| ' + str(p_values[i])[0] + ' '
        q_values[i] = '| ' + str(q_values[i])[0] + ' '
        r_values[i] = '| ' + str(r_values[i])[0] + ' '
        a_values[i] = '| ' + str(a_values[i])[0] + ' '
        b_values[i] = '| ' + str(b_values[i])[0] + ' |'

    # Construct table elements
    divider = '+---' * 5 + '+'
    header = '| p | q | r | A | B |'

    # Print table
    print(divider + '\n' + header + '\n' + divider)

    for i in range(8):
        print(
            p_values[i] + q_values[i] + r_values[i]
            + a_values[i] + b_values[i] + '\n' + divider
        )


main()
