# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 8
#
# Returns the set of students who completed 5001 but need 5002.
# -----------------------------------------------------------------------------

def needs_5002(roster_1, roster_2):
    output = roster_1.difference(roster_2)
    return output

def main():

    set_5001 = {'Andy', 'Beth', 'Chuck', 'Derek', 'Emily'}
    set_5002 = {'Beth', 'Frank', 'Emily', 'Greg', 'Helen'}

    print(needs_5002(set_5001, set_5002))


main()