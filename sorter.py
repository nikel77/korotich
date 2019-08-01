list = [1, 7, 3, 'sugar', 2, 'salt', 1, 'sun', 2, 'forest', 54, 13, 'sun', 6, 'wind', 6, 1, 13]


def sorter(input):
    num_list = []
    str_list = []
    for element in input:
        if type(element) is int and element % 2 != 0 and element * 2 not in num_list:
            num_list.append(element * 2)
        if type(element) is str and element not in str_list:
            str_list.append(element)

    new_dict = {}
    i = 1
    for element in str_list:
        new_dict.update({'string{}'.format(i): str_list[i - 1]})
        i += 1

    return num_list, new_dict


print(sorter(list))


# for key in sorted(new_dict):
#    print (key, new_dict[key])

def sorter1(input):
    num_list = []
    str_list = []
    for element in input:
        if type(element) is int and element % 2 != 0 and element * 2 not in num_list:
            num_list.append(element * 2)
        if type(element) is str and element not in str_list:
            str_list.append(element)

    key_list = []
    for i in range(1, len(str_list) + 1):
        key_list.append('string{}'.format(i))
    new_dict = {key: value for key, value in zip(key_list, str_list)}

    return num_list, new_dict


print(sorter1(list))


def sorter2(input):
    new_set = set(input)
    num_list = [element * 2 for element in new_set if isinstance(element, int) and element % 2 != 0]
    str_list = [element for element in new_set if isinstance(element, str)]

    key_list = []
    for i in range(1, len(str_list) + 1):
        key_list.append('string{}'.format(i))
    new_dict = {key: value for key, value in zip(key_list, str_list)}

    return num_list, new_dict

print(sorter2(list))
