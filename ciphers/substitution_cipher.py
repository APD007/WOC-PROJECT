import string
import random
import json
from colorama import Fore, Style

def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def generate_random_substitution_key():
    alphabet0 = (generate_alphabet_choice())
    alphabet = list(alphabet0)
    alphabet1= set(alphabet0)
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    substitution_key = dict(zip(alphabet, shuffled_alphabet))
    validate_substitution_key(substitution_key,alphabet1)
    return substitution_key

def generate_custom_substitution_key():
    alphabet0 = (generate_alphabet_choice())
    alphabet = list(alphabet0)
    alphabet1= set(alphabet0)
    substitution_key = {}

    for char in alphabet:
        user_input = input(f"Enter the substitution for '{char}': ").upper()
        substitution_key[char] = user_input.lower()
        
    validate_substitution_key(substitution_key,alphabet1)
    return substitution_key

def save_substitution_key_to_file(substitution_key):
    try:
        file_path = input("Enter the file path to save the substitution key: ")
        with open(file_path, 'w') as file:
            json.dump(substitution_key, file)
        print_color(f"Substitution key saved to {file_path}", Fore.GREEN)
    except Exception as e:
        print_color(f"An error occurred while saving the substitution key: {e}", Fore.RED)

def load_substitution_key_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            substitution_key = json.load(file)
        return substitution_key
    except FileNotFoundError:
        print_color("File not found. Please check the file path and try again.", Fore.RED)
    except Exception as e:
        print_color(f"An error occurred while loading the substitution key: {e}", Fore.RED)

def validate_substitution_key(substitution_key, alphabet):
    try:
        key_letters = set(substitution_key.keys())

        
        if not key_letters.issuperset(alphabet):
            print_color("Error: Substitution key must cover all characters of the selected alphabet.", Fore.RED)
            return False

        
        if len(set(substitution_key.values())) != len(key_letters):
            print_color("Error: Substitution key must have unique mappings.", Fore.RED)
            return False

        return True
    except Exception as e:
        print_color(f"An error occurred while validating the substitution key: {e}", Fore.RED)
        return False


def generate_alphabet_choice():
    try:
        print("Choose the type of characters in your plaintext:")
        print("1. A-Z")
        print("2. A-Z and 0-9")
        print("3. A-Z, a-z, 0-9")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            return string.ascii_uppercase
        elif choice == "2":
            return string.ascii_uppercase + string.digits
        elif choice == "3":
            return string.ascii_letters + string.digits
        else:
            print_color("Invalid choice. Using default A-Z.", Fore.YELLOW)
            return string.ascii_uppercase
    except Exception as e:
        print_color(f"An error occurred while generating the alphabet choice: {e}", Fore.RED)
        return string.ascii_uppercase

def encrypt_substitution(plaintext, substitution_key):
    try:
        encrypted_message = ""
        for char in plaintext:
            if char.isalnum():  
                substitute = substitution_key.get(char, char)
                encrypted_message += substitute
            else:
                encrypted_message += char
        return encrypted_message
    except Exception as e:
        print_color(f"An error occurred during substitution encryption: {e}", Fore.RED)
        return plaintext

def decrypt_substitution(ciphertext, substitution_key):
    try:
        reverse_key = {v: k for k, v in substitution_key.items()}
        print_color(f"\nReverse Key: {reverse_key}", Fore.CYAN)
        decrypted_message = ""
        for char in ciphertext:
            if char.isalnum():
                decrypted_char = reverse_key.get(char, char)
                decrypted_message += decrypted_char
            else:
                decrypted_message += char
        return decrypted_message
    except Exception as e:
        print_color(f"An error occurred during substitution decryption: {e}", Fore.RED)
        return ciphertext



def substitution_cipher_info():
    info = """
    ********************* Substitution Cipher Info *********************
    
    Substitution Cipher is a method of encrypting an alphabet by replacing each letter
    with another letter. The key for this cipher is a mapping of each letter to its
    substitute, creating a one-to-one correspondence between the letters of the
    plaintext and ciphertext.

    Key Generation:
    - A random key is generated by shuffling the uppercase alphabet.

    Encryption:
    - Each letter in the plaintext is substituted with its corresponding letter
      from the key.

    Decryption:
    - The process is reversed by using the inverse mapping of the key.

    Security Considerations:
    - Security relies on the secrecy of the key. If the key is compromised, the
      entire system is vulnerable.
    - Brute-force attacks are feasible due to the limited keyspace. Longer keys
      (larger alphabets) increase security.

    Note: Non-alphabetic characters are left unchanged.

    **********************************************************************
    """
    return info


