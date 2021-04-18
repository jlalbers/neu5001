'''def series_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += int('3' * i)
    return total'''

def concatenate_lists(list_1, list_2):
    output = []
    for i in range(0, len(list_1)):
        for j in range(0, len(list_2)):
            new_str = list_1[i] + ' ' +list_2[j]
            output.append(new_str)
    return output


def main():
    print(concatenate_lists(['Hello', 'take'], ['Dear', 'Sir']))

main()