import typing as tp
def func_enc(symbol: str, shift: int):
    encrypted = ""
    if symbol.isupper():
        symbol_index = ord(symbol) - ord("A")
        new_symbol = chr((symbol_index + shift) % 26 + ord("A"))
        encrypted += new_symbol
    elif symbol.islower():
        symbol_index = ord(symbol) - ord("a")
        new_symbol = chr((symbol_index + shift) % 26 + ord("a"))
        encrypted += new_symbol
    elif symbol.isdigit():
        encrypted += str(symbol)
    else:
        encrypted += symbol
    return encrypted
def func_dec(symbol: str, shift: int):
    encrypted = ""
    if symbol.isupper():
        symbol_index = ord(symbol) - ord("A")
        new_symbol = chr((symbol_index - shift) % 26 + ord("A"))
        encrypted += new_symbol
    elif symbol.islower():
        symbol_index = ord(symbol) - ord("a")
        new_symbol = chr((symbol_index - shift) % 26 + ord("a"))
        encrypted += new_symbol
    elif symbol.isdigit():
        encrypted += str(symbol)
    else:
        encrypted += symbol
    return encrypted

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    encrypted = ""
    for symbol in plaintext:
       encrypted+=func_enc(symbol,shift)
    return encrypted


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    for symbol in ciphertext:
        plaintext+=func_dec(symbol,shift)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
print(decrypt_caesar("SBWKRQ",3))