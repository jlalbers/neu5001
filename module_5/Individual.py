def add(first, second):

    return first + second

def subtract(first, second):

    return first - second

def multiply(first, second):

    return first * second

def divide(first, second):

    return first / second

def main():

    first_number = float(input('Enter the first number: '))
    second_number = float(input('Enter the second number: '))
    

    print('''Select the operation you want to perform:\n\n
             0. Add\n
             1. Subtract\n
             2. Multiply\n
             3. Divide\n
             4. Stop''')

    operation = int(input('Operation: '))

    while operation != 4:

        while operation < 0 or operation > 3:
            operation = int(input('Please enter 0, 1, 2, 3, or 4: '))

        if operation == 0:
            result = add(first_number, second_number)
            print(first_number, '+', second_number, '=', result)

        elif operation == 1:
            result = subtract(first_number, second_number)
            print(first_number, '-', second_number, '=', result)
        
        elif operation == 2:
            result = multiply(first_number, second_number)
            print(first_number, '*', second_number, '=', result)
        
        elif operation == 3:
            result = divide(first_number, second_number)
            print(first_number, '/', second_number, '=', result)

        print('''Select the operation you want to perform:\n\n
             0. Add\n
             1. Subtract\n
             2. Multiply\n
             3. Divide\n
             4. Stop''')

        operation = int(input('Operation: '))

        
main()

    