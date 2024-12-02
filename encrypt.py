#WARNING: These are easy to decode.

def caesar_cipher_encrypt(s, shift):
    result = ""
    for char in s:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result
#WARNING: These are easy to decode.
if __name__ == "__main__":
    daror = input("Encrpyt: ")
    anor = int(input("(0-25): "))
    encrypted = caesar_cipher_encrypt(daror, anor)
    print("Encrypted Text:", encrypted)

#WARNING: These are easy to decode.
