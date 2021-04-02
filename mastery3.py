# ------------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Mastery 2 Problem 3
#
# Given a binary pattern that contains ‘?’ wildcard character at few positions, 
# find all possible 
# combinations of binary strings that can be formed by replacing the wildcard 
# character by either 0 or 1 using recursion. 
# ------------------------------------------------------------------------------

def string_maker(binary_str: str) -> str:
    '''
    Function: string_maker\n
    Parameters: binary_str - string of bits with one or more wildcard "?" char\n
    Outputs: comma-delineated string with all possibilities if "?" replaced
    with "0" or "1"
    '''
    if '?' not in binary_str:
        return binary_str
    elif '?' in binary_str:
        options = binary_str.split('?', 1)
        return (string_maker(options[0] + '0' + options[1]) + ',' +
            string_maker(options[0] + '1' + options[1])
        )


def string_list(string: str) -> list:
    '''
    Function: string_list\n
    Parameters: string - comma-delineated string\n
    Outputs: list of strings
    '''
    output = string.split(',')
    return output


def main():
    print(string_list(string_maker('01?10?11')))


main()
