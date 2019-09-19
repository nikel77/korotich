"""Function 'emirp_check' checks if the input number is emirp"""
"""Function 'emirp_range_check' returns all emirp numbers in given range"""
"""Both of these functions use 'prime_check' function to check if the number
prime or not"""

def prime_check(number):
    for i in range(2, number):
        if number % i != 0:
            continue
        else:
            return
    return number


def emirp_check():
    number = int(input('Input any number: '))
    number = prime_check(number)

    if number is not None:
        string = str(number)
        new_string = string[::-1]

        new_number = prime_check(int(new_string))

        if new_number is not None:
            print('The number {} is an emirp number'.format(number))
        else:
            print('{} is not an emirp number'.format(number))
    else:
        print('{} is not an emirp number'.format(number))

    return


emirp_check()


def emirp_range_check():
    from_number = int(input('Input the first number of range: '))
    to_number = int(input('Input the last number of range: '))
    emirp_list = []
    for number in range(from_number, to_number + 1):
        number = prime_check(number)

        if number is not None:
            string = str(number)
            new_number = None
            new_string = string[::-1]

            if new_string != string:
                new_number = prime_check(int(new_string))

            if new_number is not None:
                emirp_list.append(number)
    print(emirp_list)
    return emirp_list


emirp_range_check()