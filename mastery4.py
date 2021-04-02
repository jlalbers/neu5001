# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Mastery 2 Problem 4
#
# Function that returns a set of the unique values of multiple dictionaries
# stored in a list.
# -----------------------------------------------------------------------------
def unique_values(lst: list) -> set:
    '''
    Function: unique_values\n
    Parameters: lst - list of one or more dictionaries\n
    Outputs: set of unique values from dictionaries
    '''
    output = set()
    for item in lst:
        value = set(item.values())
        output = output.union(value)
    return output

def main():

    print(unique_values([{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]))

main()
