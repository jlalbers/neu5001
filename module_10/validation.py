# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 10 Practice 1
#
# Performs multiplication with different types.
# -----------------------------------------------------------------------------

def validation(integer, floating):
    if not isinstance(integer, int):
        raise TypeError('"integer" must be an integer.')
    elif integer > -1:
        raise ValueError('"integer" must be negative.')

    if not isinstance(floating, float):
        raise TypeError('"floating" must be a float.')
    elif floating <= 0 or floating >= 1000:
        raise ValueError('"floating" must be >0 and <1000.')

    return integer * floating


def main():

    print(validation(-1, 1000.0))


main()