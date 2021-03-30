# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 10 Practice 3
#
# Returns True if a course number is part of the Align bridge.
# -----------------------------------------------------------------------------

def is_bridge(course):
    if not isinstance(course, int):
        raise TypeError('Course must be an integer.')
    else:
        if course in [5001, 5002, 5003, 5004, 5005, 5006]:
            out = True
        else:
            out = False

    return out

def main():

    try:
        courses = [5001, 5002, 5003, 5004.0, 5005, 5006, 5007]
        for i in courses:
            print(is_bridge(i))

    except TypeError as ex:
        print('Error at ' + str(i) + ': ', ex)
        
main()
