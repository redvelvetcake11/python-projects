"""
This module provides a Caesar cipher encryption and decryption methods.
"""

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def encrypt(string, shift):
    """
    Encrypts the given string using a Caesar cipher with the given shift.

    :param string: The string to be encrypted.
    :param shift: The amount of characters to shift.
    :return: The encrypted string.
    """
    ciphered_text = ''
    shifted_symbols = symbols[shift:] + symbols[:shift]

    for i in string:
        if i in symbols:
            ciphered_text += shifted_symbols[symbols.index(i)]
        else:
            ciphered_text += i

    return ciphered_text

def decrypt(string, shift):
    """
    Decrypts the given string using a Caesar cipher with the given shift.

    :param string: The string to be decrypted.
    :param shift: The amount of characters to shift.
    :return: The decrypted string.
    """
    ciphered_text = ''
    shifted_symbols = symbols[-shift:] + symbols[:-shift]

    for i in string:
        if i in symbols:
            ciphered_text += shifted_symbols[symbols.index(i)]
        else:
            ciphered_text += i

    return ciphered_text

if __name__ == '__main__':
    string = input("Enter a string: ")
    mode = input("Select a mode (e to encrypt and d to decrypt): ")
    shift = int(input("How much to shift? "))

    if mode == 'e':
        print(encrypt(string, shift))
    elif mode == 'd':
        print(decrypt(string, shift))
