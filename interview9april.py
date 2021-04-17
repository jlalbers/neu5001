'''def flatten_array(array, output=[]):
    for item in array:
        if not isinstance(item, list):
            output.append(item)
        else:
            flatten_array(item, output)
    return output

print(flatten_array([[1], [2, 3], [4], [3, [2, 4]]]))'''

def case_flip(lst, i=0):
    if i == len(lst) - 1:
        lst[i] = lst[i].upper()
    else:
        lst[i] = lst[i].upper()
        case_flip(lst, i + 1)


test = ['abc','vggh','gfyj']
case_flip(test)
print(test)
