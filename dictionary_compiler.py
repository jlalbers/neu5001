# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Class Dictionary: Compiler
#
# This program compiles all the individual dictionary .txt files into a single
# dictionary stored in a variable in another Python file.
# -----------------------------------------------------------------------------

import os
import json

def get_files(directory=os.getcwd()):
    cwd_list = os.listdir(directory).copy()
    files_list = []
    for i in range(len(cwd_list)):
        if 'spring2021_dictionary' in cwd_list[i]:
            files_list.append(cwd_list[i])
    return files_list


def append_class_dictionary(filename, dictionary):
    input_dict = open(filename)
    for line in input_dict.readlines():
        key, value, keywords = line.split(':::')
        keyword_list = [x.strip() for x in keywords.split(',')]
        if key not in dictionary:
            dictionary[key] = [[value], keyword_list]
        else:
            dictionary[key][0].append(value)
            dictionary[key][1].extend(keyword_list)
    input_dict.close()


def main():
    class_dict_file = open('class_dictionary.txt', 'w')
    dict_list = get_files()
    class_dict = dict()
    for file in dict_list:
        append_class_dictionary(file, class_dict)
    class_dict_file.write(str(class_dict))
    class_dict_file.close()
    print(class_dict)


main()
            
            