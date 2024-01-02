import string
from utils import input_output
import random
from colorama import Fore, Style

def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL) 
    
def generate_homophonic_key():
    alphabet = string.ascii_letters + string.digits + string.punctuation + string.whitespace
    homophonic_key = {}

    
    used_mappings = set()

    
    character_frequencies = {
        'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31,
        'N': 6.95, 'S': 6.28, 'R': 6.02, 'H': 5.92, 'D': 4.32,
        'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30,
        'Y': 2.11, 'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49,
        'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10,
        'Z': 0.07,
        'a': 8.12, 'o': 7.68, 'i': 7.31, 'n': 6.95, 's': 6.28,
        'r': 6.02, 'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88,
        'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11, 'w': 2.09,
        'g': 2.03, 'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': 0.69,
        'x': 0.17, 'q': 0.11, 'j': 0.10, 'z': 0.07,
        '0': 4.0, '1': 3.5, '2': 3.0, '3': 2.5, '4': 2.0,
        '5': 1.5, '6': 1.0, '7': 0.5, '8': 0.3, '9': 0.2, '!': 1.0, '@': 0.5, '#': 0.3, '$': 0.2,
        '%': 0.1, '&': 0.1, '*': 0.1, '(': 0.1, ')': 0.1,
        '.': 1.0, ',': 0.8, ';': 0.5, ':': 0.5, '?': 0.5,
        "'": 0.4, '"': 0.4, '/': 0.2, '\\': 0.2, '|': 0.1,
        '-': 0.6, '_': 0.3, '=': 0.2, '+': 0.2, '<': 0.1,
        '>': 0.1, '[': 0.1, ']': 0.1, '{': 0.1, '}': 0.1,
        '`': 0.1, '~': 0.1 , ' ' : 0.1
    }

    for char in alphabet:
        
        list_size = max(1, round(character_frequencies.get(char, 0) * 2))
        homophonic_key[char] = list(set(generate_homophonic_char(char, used_mappings) for _ in range(list_size)))

    return homophonic_key

def generate_homophonic_char(base_char, used_mappings):
    while True:
        
        mapping = f"{random.randint(1, 9999):04}"

        
        if mapping not in used_mappings:
            used_mappings.add(mapping)
            return mapping

def homophonic_cipher_info():
    info = """
    ********************* Homophonic Cipher Info *********************

    Homophonic Cipher is a substitution cipher where each character of the
    plaintext may correspond to one or more characters in the ciphertext.

    Encryption:
    - Each character in the plaintext is replaced with one of the possible
      ciphertext characters based on a predefined or custom frequency.

    Decryption:
    - The process is reversed by using the inverse mapping of the key.

    Key Generation:
    - Keys can be generated randomly or based on custom frequencies.

    Security Considerations:
    - Homophonic ciphers can provide better security compared to simple substitution
      ciphers. However, the security relies on the secrecy of the key.
    - The use of multiple characters for each plaintext character increases the
      complexity for attackers.

    Note: Non-alphabetic characters are left unchanged.

    **********************************************************************
    """
    return info



def encrypt_homophonic(plaintext, homophonic_key):
    ciphertext = ""
    for char in plaintext:
        if char in homophonic_key:
            homophonic_char = random.choice(homophonic_key[char])
            ciphertext += homophonic_char
        else:
            ciphertext += char
    return ciphertext

def decrypt_homophonic(ciphertext, homophonic_key):
    reverse_mapping = {number: letter for letter, numbers in homophonic_key.items() for number in numbers}
    
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        segment = ""
        found = False
        while i < len(ciphertext) and ciphertext[i].isalnum():
            segment += ciphertext[i]
            i += 1
            if segment in reverse_mapping:
                plaintext += reverse_mapping[segment]
                found = True
                break
        if not found:
            plaintext += segment
            i += 1
    return plaintext

def load_homophonic_key_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            homophonic_key_str = file.read()
        homophonic_key = eval(homophonic_key_str)
        return homophonic_key
    except FileNotFoundError:
        print_color("File not found. Please check the file path and try again.", Fore.RED)
    except Exception as e:
        print_color(f"An error occurred while loading the homophonic key: {e}", Fore.RED)

def save_homophonic_key_to_file(homophonic_key, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(str(homophonic_key))
        print_color(f"Homophonic key saved to {file_path}", Fore.GREEN)
    except Exception as e:
        print_color(f"An error occurred while saving the homophonic key: {e}", Fore.RED)

def handle_manual_key_entry():
    try:
        homophonic_key = input_output.get_dict_input("Enter a mapping (e.g., {'A': ['01', '02']}): ")
        print(f"Current Mapping: {homophonic_key}")
        return homophonic_key
    except Exception as e:
        print_color(f"An error occurred during manual key entry: {e}", Fore.RED)
        