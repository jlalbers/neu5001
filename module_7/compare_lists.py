'''
Jameson Albers
CS 5001, Spring 2021
Module 7 Practice 8

Returns True if the items in two lists are identical and in the same order.'''

def compare_lists(list_1, list_2):

    are_same = True

    if len(list_1) != len(list_2):
        are_same = False

    else:
        for x,y in zip(list_1, list_2):
            if x != y:
                are_same = False
                break

    return are_same


def main():

    print(compare_lists(['a', 'b', 'c'], ['a', 'b', 'c']))


main()
