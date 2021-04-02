# -----------------------------------------------------------------------------
# Jameson Albers
# CS 5001, Spring 2021
# Mastery 2 Problem 1
#
# Open a text file and count the number of words in the file, then write the
# number of words to a different file.
# -----------------------------------------------------------------------------

def count_words(filename: str) -> int:
    '''
    Function: count_words\n
    Parameters: filename - string of the filename to open\n
    Outputs: number of words in the file as an int
    '''
    file = open(filename)
    word_count = 0
    for line in file.readlines():
        words = line.split(' ')
        word_count += len(words)
    file.close()
    return word_count


def write_words(new_file: str, integer: int) -> None:
    '''
    Function: write_words\n
    Parameters: filename - str of filename to open, integer - int value to 
    write to file\n
    Outputs: prints "Write successful." if file successfully written
    '''
    output = open(new_file, 'w')
    output.write(str(integer))
    output.close()
    print('Write successful.')


def main():
    try:
        test = input('Enter filename: ')
        number = count_words(test)
        write_words('output.txt', number)
        test2 = open('output.txt')
        print_words = test2.read()
        print(print_words)
        test2.close()

    except FileNotFoundError:
        print('The file was not found.')
    except PermissionError:
        print('You do not have permission to open this file')
    except OSError:
        print('Something went wrong while opening the file')


main()