"""Function 'emirp_check' checks if the input number is emirp
Function 'emirp_range_check' returns all emirp numbers in given range
Both of these functions use 'prime_check' function to check if the number
prime or not"""


def prime_check(number):
    for i in range(2, number):
        if number % i != 0:
            continue
        else:
            return False
    return True


def emirp_check():
    number = int(input('Input any number: '))

    if prime_check(number) is True:
        string = str(number)

        if prime_check(int(string[::-1])) is True:
            print('The number {} is an emirp number'.format(number))
            return
    print('{} is not an emirp number'.format(number))
    return


emirp_check()


def emirp_range_check():
    from_number = int(input('Input the first number of range: '))
    to_number = int(input('Input the last number of range: '))
    emirp_list = []

    for number in range(from_number, to_number + 1):

        if prime_check(number) is True:
            string = str(number)
            new_string = str(number)[::-1]

            if new_string != string:

                if prime_check(int(new_string)) is True:
                    emirp_list.append(number)

    print(emirp_list)
    return emirp_list


emirp_range_check()
