# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Mastery 2 Problem 2
#
# Define one class which will have the following methods:
# Function to find a pair of elements (indices of the two numbers) from a given
# array whose sum equals a specific target number. Assume that only one distinct
# pair is present in the list whose sum is exactly equal to the target.
# Input:numbers=[20,10,40,50,60,70],target=50
# Output: 1, 2
# Write a Python program to get all possible unique subsets from a set of
# distinct integers.
# Input:[4,5,6]
# Output: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
# -----------------------------------------------------------------------------

class Fun:

    def __init__(self):
        self.having_fun = 'Yes'

    def find_pair(self, numbers: list, target: int) -> tuple:
        '''
        Method: find_pair\n
        Parameters: list of integers, target integer\n
        Outputs: tuple of indeces of list items whose sum is the target
        '''
        if isinstance(numbers, list) and isinstance(target, int):
            for num in numbers:
                for i in range(numbers.index(num)+1, len(numbers)):
                    if num + numbers[i] == target:
                        output = (numbers.index(num), i)
                        break
            return output
        else:
            raise TypeError

    def power_set(self, integers: list) -> list:
        '''
        Method: power_set\n
        Inputs: list of three integers\n
        Outputs: power set of those integers as a list
        '''
        output = [[]]
        last_set = []
        for num in integers:
            output.append([num])
            if num != integers[-1]:
                for i in range(integers.index(num)+1, len(integers)):
                    sett = list((num, integers[i]))
                    output.append(sett)
            last_set.append(num)
        output.append(last_set)
        return output

def main():
    test = Fun()
    output_1 = test.find_pair([20,10,40,50,60,70], 50)
    print(output_1)
    output_2 = test.power_set([4,5,6])
    print(output_2)


main()
                


    

