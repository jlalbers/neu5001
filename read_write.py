import os

def read_write():
    try:
        choice = '1'
        while choice != 'q':
            choice = input('Do you want to read a file (r) or write to a file (w)? Enter (q) to quit: ')
            if choice.lower() != 'r' and choice != 'w' and choice != 'q':
                print('Please select a valid option.')
            elif choice.lower() == 'r':
                filename = input('Enter the file to read: ')
                read_file = open(filename, 'r')
                for line in read_file.readlines():
                    print(line)
                read_file.close()
            elif choice.lower() == 'w':
                filename = input('Enter the file to create: ')
                write_file = open(filename, 'w')
                contents = input('Enter the content to write to the file:\n')
                write_file.write(contents)
                write_file.close()

    except FileNotFoundError:
        print('The file', filename, 'was not found.')
    except PermissionError:
        print('You do not have permission to open', filename)
    except OSError:
        print('Something went wrong while accessing', filename)
    

read_write()