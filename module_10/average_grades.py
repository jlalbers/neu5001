# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Module 10 Practice 5
#
# Reads grades from a file and returns the average.
# -----------------------------------------------------------------------------

def average_grades(filename):
    try:
        total = 0
        count = 0
        grades = open(filename)
        for grade in grades:
            total += float(grade.strip())
            count += 1

        grades.close()
        
        return total / count

    except FileNotFoundError:
        print('File not found:', filename)
    except PermissionError:
        print('Permission denied for', filename)
    except OSError:
        print('Something went wrong while reading', filename)


def main():

    print(average_grades('grades.txt'))


main()
