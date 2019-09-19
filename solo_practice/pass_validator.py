"""This function checks if the password has valid format:
- length from 5 to 10 symbols
- no spaces
- at least one digit
- at least on special character"""

from string import punctuation, digits


def pass_val():
    password = input('Input password: ')
    int_check = False
    punct_check = False
    result = False
    if (5 <= len(password) <= 10) and " " not in password:
        for symbol in password:
            if symbol in digits:
                int_check = True
            if symbol in punctuation:
                punct_check = True
        result = int_check and punct_check
    return result


print(pass_val())
