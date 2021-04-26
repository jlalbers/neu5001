# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Class Dictionary: Compiler
#
# This program compiles all the individual dictionary .csv files into a single
# dictionary stored as a text file.
# -----------------------------------------------------------------------------

import os
import csv

def get_files(directory=os.getcwd()):
    # Returns a list of filenames using filename standerd from dictionary
    # builder
    cwd_list = os.listdir(directory).copy()  # Scrapes CWD for filenames
    files_list = []  # Initialize output list
    for i in range(len(cwd_list)):
        if 'spring2021_dictionary' in cwd_list[i]:
            # Adds filename to list if it has the template format
            files_list.append(cwd_list[i])  
    return files_list


def append_class_dictionary(filename, dictionary):
    # Adds information from individual dictionaries to the class dictionary
    input_dict = open(filename)  # Opens individual dictionary
    # Initialize csv reader object
    reader = csv.reader(input_dict, delimiter=',', quotechar='"')
    for line in reader:  # Reads each line in csv file
        key, value, keywords = line  # Gets word, definition, and keywords
        # Create list of keywords
        keyword_list = [x.strip() for x in keywords.split(',')]
        if key not in dictionary:
            # Add new entry to dictionary
            dictionary[key] = [[value], keyword_list]
        else:
            # Add new value and keywords to existing entry
            dictionary[key][0].append(value)
            dictionary[key][1].extend(keyword_list)
    input_dict.close()


def main():
    # Create class dictionary/overwwrite existing dictionary
    class_dict_file = open('class_dictionary.txt', 'w') 
    dict_list = get_files()
    class_dict = dict()
    for file in dict_list:
        # Add words from individual dictionary to class dictionary
        append_class_dictionary(file, class_dict)
    # Write class dictionary to text file
    class_dict_file.write(str(class_dict))
    class_dict_file.close()
    print(class_dict)


main()
            
            