"""This program encrypts messages and the second one decrypts them"""

def encrypt():
    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a']
    sentence = input("input message to crypt: ")
    new_sentence = ""
    for letter in sentence:
        if letter in alphabeth:
            new_letter = alphabeth[alphabeth.index(letter) + 1]
        else:
            new_letter = letter
        new_sentence += new_letter
    return new_sentence

print(encrypt())

def decrypt():
    alphabeth = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    sentence = input("input encrypted message: ")
    new_sentence = ""
    for letter in sentence:
        if letter in alphabeth:
            new_letter = alphabeth[alphabeth.index(letter) - 1]
        else:
            new_letter = letter
        new_sentence += new_letter
    return new_sentence

print(decrypt())