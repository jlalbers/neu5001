def test_one_parameter(args, func, expected):

    passed = True

    for i in range(len(args)):
        result = func(args[i])
        if result != expected[i]:
            passed = False
            print('Error at test ' + str(i+1))

    if passed == True:
        print('Function passed!')
    else:
        print('Function failed.')

    return passed


def main():

    test_x = 

    tests = []
    arguments = []
    expecteds = []

    for test in tests:
        arguments.append(test[0])
        expecteds.append(test[1])

    test_one_parameter(arguments, func, expecteds)


main()