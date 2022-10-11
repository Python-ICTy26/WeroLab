from caesar import *
def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    ciphertext = ""
    i = len(keyword)
    for symbol in plaintext:
        if len(keyword) < i + 1:
            i = 0
        if symbol.isupper():
            ciphertext += func_enc(symbol, ord(keyword[i]) - ord("A"))
        elif symbol.islower():
            ciphertext += func_dec(symbol, ord(keyword[i]) - ord("a"))
        else:
            ciphertext += str(symbol)
        i += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    plaintext = ""
    i = len(keyword)
    for symbol in ciphertext:
        if len(keyword) < i + 1:
            i = 0
        if symbol.isupper():
           plaintext+=func1(symbol,ord(keyword[i]) - ord("A"))
        elif symbol.islower():
            plaintext+=func1(symbol,ord(keyword[i]) - ord("a"))
        else:
            plaintext += str(symbol)
        i += 1
    return plaintext
#print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))