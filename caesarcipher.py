symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def encrypt(string, shift):
    ciphered_text = ''
    shifted_symbols = symbols[shift:] + symbols[:shift]

    for i in string:
        if i in symbols:
            ciphered_text += shifted_symbols[symbols.index(i)]
        else:
            ciphered_text += i

    return ciphered_text

def decrypt(string, shift):
    ciphered_text = ''
    shifted_symbols = symbols[-shift:] + symbols[:-shift]

    for i in string:
        if i in symbols:
            ciphered_text += shifted_symbols[symbols.index(i)]
        else:
            ciphered_text += i

    return ciphered_text


string = input("Enter a string: ")
mode = input("Select a mode (e to encrypt and d to decrypt): ")
shift = int(input("How much to shift? "))

if mode == 'e':
    print(encrypt(string, shift))
elif mode == 'd':
    print(decrypt(string, shift))
