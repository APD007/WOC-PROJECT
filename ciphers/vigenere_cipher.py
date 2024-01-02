from colorama import Fore, Style
import string
import random

def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def display_feedback(message, success=True):
    if success:
        print_color(f"Success: {message}", Fore.GREEN)
    else:
        print_color(f"Error: {message}", Fore.RED)



def encrypt_vigenere(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            char_copy = char
            shift = ord(key[key_index % len(key)]) - ord('A')
            encrypted_char = chr((ord(char.upper()) + shift - ord('A')) % 26 + ord('A'))
            if char_copy.isupper():
                ciphertext += encrypted_char
            else:
                ciphertext += encrypted_char.lower()
            key_index += 1
        else:
            ciphertext += char

    return ciphertext

def decrypt_vigenere(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            char_copy = char
            shift = ord(key[key_index % len(key)]) - ord('A')
            decrypted_char = chr((ord(char.upper()) - shift - ord('A')) % 26 + ord('A'))
            if char_copy.isupper():
                plaintext += decrypted_char
            else:
                plaintext += decrypted_char.lower()
            key_index += 1
        else:
            plaintext += char

    return plaintext

def save_key_to_file(key, filename):
    try:
        with open(filename, 'w') as file:
            file.write(key)
        display_feedback(f"Key saved to {filename}", success=True)
    except Exception as e:
        display_feedback(f"An error occurred while saving the key: {e}", success=False)

def read_key_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        display_feedback("File not found. Please check the file path and try again.", success=False)
    except Exception as e:
        display_feedback(f"An error occurred while reading the key: {e}", success=False)

def generate_random_key(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def generate_repeating_keyword(keyword, length):
    repetitions = length // len(keyword) + 1
    return (keyword * repetitions)[:length]

def vigenere_cipher_info():
    info = """
    ********************* Vigenère Cipher Info *********************
    
    Vigenère Cipher is a method of encrypting alphabetic text using a simple form
    of polyalphabetic substitution. A polyalphabetic cipher uses multiple substitution
    alphabets to encrypt the text, making it more resistant to frequency analysis.

    Encryption:
    - The key for Vigenère Cipher is a keyword, which is repeatedly appended to match
      the length of the plaintext.
    - Each letter of the plaintext is then shifted based on the corresponding letter
      of the keyword.

    Decryption:
    - To decrypt, the recipient must know the keyword.
    - Each letter of the ciphertext is shifted backward based on the corresponding
      letter of the keyword.

    Security Level:
    - Vigenère Cipher is stronger than simple substitution ciphers, as the same letter
      can be encrypted to different letters at different positions in the message.
    - However, it can still be susceptible to frequency analysis, especially if the
      keyword is short or easily guessable.

    ******************************************************************
    """
    return info


