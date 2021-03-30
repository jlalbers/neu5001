# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 9
#
# Returns the set of students who completed 5002 but need 5001.
# -----------------------------------------------------------------------------

def needs_5001(roster_1, roster_2):
    output = roster_2.difference(roster_1)
    return output

def main():

    set_5001 = {'Andy', 'Beth', 'Chuck', 'Derek', 'Emily'}
    set_5002 = {'Beth', 'Frank', 'Emily', 'Greg', 'Helen'}

    print(needs_5001(set_5001, set_5002))


main()