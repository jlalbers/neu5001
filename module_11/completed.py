# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 11 Practice 10
#
# Returns the set of students who completed 5002 and 5001.
# -----------------------------------------------------------------------------

def completed(roster_1, roster_2):
    output = roster_2.intersection(roster_1)
    return output

def main():

    set_5001 = {'Andy', 'Beth', 'Chuck', 'Derek', 'Emily'}
    set_5002 = {'Beth', 'Frank', 'Emily', 'Greg', 'Helen'}

    print(completed(set_5001, set_5002))


main()