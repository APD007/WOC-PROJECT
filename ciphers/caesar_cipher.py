

import string
import random
import time
from colorama import Fore, Style

def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)
    
def display_feedback(message, success=True):
    if success:
        print_color(f"Success: {message}", Fore.GREEN)
    else:
        print_color(f"Error: {message}", Fore.RED) 

def generate_alphabet():
    try:
        custom_alphabet_option = input("1. A-Z\n2. A-Z and 0-9\n3. ASCII (0-127)\nEnter your choice: ")

        if custom_alphabet_option == "1":
            custom_alphabet = string.ascii_uppercase
        elif custom_alphabet_option == "2":
            custom_alphabet = string.ascii_uppercase + string.digits
        elif custom_alphabet_option == "3":
            custom_alphabet = "".join([chr(i) for i in range(128)])
        else:
            print_color("Invalid choice. Using default A-Z and 0-9.", Fore.YELLOW)
            custom_alphabet = string.ascii_uppercase + string.digits

        if not validate_custom_alphabet(custom_alphabet):
            return generate_alphabet()

        return custom_alphabet
    except Exception as e:
        print_color(f"An error occurred while generating the alphabet: {e}", Fore.RED)


def generate_custom_alphabet():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    try:
        custom_alphabet_option = input("1. Do you want to generate a random custom alphabet?\n2. Do you want to enter it manually?\n3. Do you want to import it from your file system\nEnter your choice: (1/2/3) ")
    
        if custom_alphabet_option == "1":
            custom_alphabet = ''.join(random.sample(alphabet, len(alphabet)))
            print(f"Generated Random Custom Alphabet: {custom_alphabet}")
        
            save_custom_alphabet = input("Do you want to save this custom alphabet to a file? (yes/no): ").lower()
            if save_custom_alphabet == "yes":
                save_custom_alphabet_to_file(custom_alphabet)
            
        elif custom_alphabet_option == "2":
            custom_alphabet = input("Enter Custom alphabet: ").upper()
        
        elif custom_alphabet_option == "3":
            custom_alphabet_path = input("Enter the file path of the custom alphabet: ")
            custom_alphabet = read_custom_alphabet_from_file(custom_alphabet_path)
        
        else:
            print("Invalid choice. Please try again.")

        if not validate_custom_alphabet(custom_alphabet):
            return generate_custom_alphabet()
        return custom_alphabet
    except Exception as e:
        print_color(f"An error occurred while generating the alphabet: {e}", Fore.RED)

def validate_custom_alphabet(custom_alphabet):
    if len(custom_alphabet) != len(set(custom_alphabet)):
        print_color("Invalid custom alphabet: Duplicate characters are not allowed.", Fore.RED)
        return False
    return True


def save_custom_alphabet_to_file(custom_alphabet):
    try:
        file_path = input("Enter the file path to save the custom alphabet: ")
        with open(file_path, 'w') as file:
            file.write(custom_alphabet)
        print_color(f"Custom alphabet saved to {file_path}", Fore.GREEN)
    except Exception as e:
        print_color(f"An error occurred while saving the custom alphabet: {e}", Fore.RED)

def read_custom_alphabet_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            custom_alphabet = file.read().strip()
        return custom_alphabet
    except FileNotFoundError:
        print_color("File not found. Please check the file path and try again.", Fore.RED)
    except Exception as e:
        print_color(f"An error occurred while reading the custom alphabet: {e}", Fore.RED)


def encrypt(message, shift,  custom_alphabet=None, rounds=1):
    if custom_alphabet:
        alphabet = custom_alphabet
    else:
        alphabet = string.ascii_uppercase + string.digits

    result_left = message
    result_right = message

    for _ in range(rounds):
        
        result_left = _encrypt_round_left(result_left, shift, alphabet)
        print(f"Intermediate Result (Left Shift - Round {_ + 1}): {result_left}")
        time.sleep(0.5)

        
        result_right = _encrypt_round_right(result_right, shift, alphabet)
        print(f"Intermediate Result (Right Shift - Round {_ + 1}): {result_right}")
        time.sleep(0.5)

    return result_left, result_right

def _encrypt_round_left(message, shift, alphabet):
    result = ""
    for char in message:
        if char.upper() in alphabet:
            index = (alphabet.index(char.upper()) - shift) % len(alphabet)
            result += alphabet[index].lower() if char.islower() else alphabet[index]
        elif char.isdigit():
            index = (int(char) - shift) % 10
            result += str(index)
        else:
            result += char
    return result

def _encrypt_round_right(message, shift, alphabet):
    result = ""
    for char in message:
        if char.upper() in alphabet:
            index = (alphabet.index(char.upper()) + shift) % len(alphabet) 
            result += alphabet[index].lower() if char.islower() else alphabet[index]
        elif char.isdigit():
            index = (int(char) + shift) % 10
            result += str(index)
        else:
            result += char
    return result

 

def decrypt(custom_alphabet , ciphertext, option, key_or_word=""):
    if custom_alphabet:
        alphabet = custom_alphabet
    else:
        alphabet = string.ascii_uppercase + string.digits

   

    if option == 1:  
        known_shift = int(key_or_word)
        result_left = ""
        result_right = ""

        
        shift_left = -known_shift
        for char in ciphertext:
            if char.isalpha():
                index = (custom_alphabet.index(char.upper()) - shift_left) % len(custom_alphabet)
                result_left += custom_alphabet[index].lower() if char.islower() else custom_alphabet[index]
            elif char.isdigit():
                index = (custom_alphabet.index(char) - shift_left) % len(custom_alphabet)
                result_left += custom_alphabet[index]
            else:
                result_left += char

        
        shift_right = known_shift
        for char in ciphertext:
            if char.isalpha():
                index = (custom_alphabet.index(char.upper()) - shift_right) % len(custom_alphabet)
                result_right += custom_alphabet[index].lower() if char.islower() else custom_alphabet[index]
            elif char.isdigit():
                index = (custom_alphabet.index(char) - shift_right) % len(custom_alphabet)
                result_right += custom_alphabet[index]
            else:
                result_right += char
        print_color("\nDecrypting...", Fore.GREEN)
        print_color(f"🠞 {known_shift} (🠜 {26 - known_shift}))\tLeft Shift: {result_left}",Fore.YELLOW)
        print_color(f"🠞 {26 - known_shift} (🠜 {known_shift}))\tRight Shift: {result_right}" , Fore.YELLOW)
        

    elif option == 2:  
        print_color("Brute-force decryption results:" , Fore.GREEN)
        max_shift_digits = len(str(len(alphabet)))
        shift_format = "🠞 {:-<" + str(max_shift_digits) + "} (🠜 {:-<" + str(max_shift_digits) + "})"
        print_color("\nDecrypting...", Fore.GREEN)
        for current_shift in range(len(alphabet)):
            shift = -current_shift
            result = ""
            for char in ciphertext:
                if char.isalpha():
                    index = (custom_alphabet.index(char.upper()) - shift) % len(custom_alphabet)
                    result += custom_alphabet[index].lower() if char.islower() else custom_alphabet[index]
                elif char.isdigit():
                    index = (custom_alphabet.index(char) - shift) % len(custom_alphabet)
                    result += custom_alphabet[index]
                else:
                    result += char
                    
            
            print_color(shift_format.format(-shift, 26 + shift) + f"\t{result}" , Fore.YELLOW)


def caesar_cipher_info():
    info = """
    ********************* Caesar Cipher Info *********************
    
    The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted
    a certain number of places down or up the alphabet. It is named after Julius Caesar who
    reportedly used it to communicate with his generals.

    Security Level:
    The Caesar Cipher is a very basic and easily breakable encryption method. It can be
    easily decrypted using brute force or frequency analysis.
    """
    return info
