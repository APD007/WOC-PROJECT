from ciphers import caesar_cipher, substitution_cipher, vigenere_cipher, rsa, hill_cipher,homophonic
from key_exchange import diffie_hellman
from utils import input_output
import random
import os
import time
from colorama import Fore, Style
import math
import string    
import numpy 


def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)
    
def display_feedback(message, success=True):
    if success:
        print_color(f"Success: {message}", Fore.GREEN)
    else:
        print_color(f"Error: {message}", Fore.RED) 

def home_page():
    print_color("\n********************* Welcome to the Cryptographic System! *********************", Fore.CYAN)
    print_color("1. Private Key")
    print_color("2. Public Key")
    print_color("3. Info")
    print_color("4. Exit",Fore.RED)

def private_key_page():
    print_color("\n********************* Private Key *********************", Fore.YELLOW)
    print_color("1. Caesar Cipher")
    print_color("2. Substitution Cipher")
    print_color("3. Vigenere Cipher")
    print_color("4. Hill Cipher")
    print_color("5. Homophonic Cipher")
    print_color("6. Info")
    print_color("7. Return To Home", Fore.CYAN)
            
    print_color("8. Exit", Fore.RED)

def public_key_page():
    print_color("\n********************* Public Key *********************", Fore.MAGENTA)
    print_color("1. RSA Encryption")
    print_color("2. Diffie Hellman Key Exchange")
    print_color("3. Info")
    print_color("4. Return To Home", Fore.CYAN)
    print_color("5. Exit", Fore.RED)

def cipher_info_page():
    print_color("\n********************* Cipher Information *********************", Fore.BLUE)
    print_color("1. Caesar Cipher")
    print_color("2. Substitution Cipher")
    print_color("3. Vigenere Cipher")
    print_color("4. Hill Cipher")
    print_color("5. Homophonic Cipher")
    print_color("6. Return To Home", Fore.CYAN)
    print_color("7. Exit", Fore.RED)
    
def key_info():
    print_color("\n********************* Key Information *********************", Fore.BLUE)
    print_color("1. Private Key")
    print_color("2. Public Key")
    print_color("3. Return To Home", Fore.CYAN)
    print_color("4. Exit", Fore.RED)  
    
def private_key_info1():
    print_color("\n********************* Cipher Information *********************", Fore.BLUE)
    print_color("1. RSA Encryption")
    print_color("2. Diffie Hellman Key Exchange")
    print_color("3. Return To Home", Fore.CYAN)
    print_color("4. Exit", Fore.RED)       


def main():
    while True:
        home_page()
        choice = input_output.get_user_input("Enter your choice: ")

        if choice == "1":
            private_key_menu()
        elif choice == "2":
            public_key_menu()
        elif choice == "3":
            key_info_menu()
        elif choice == "4":
            print_color("Exiting the program.", Fore.CYAN)
            break
        else:
            display_feedback("Invalid choice. Please try again.", success=False)

def key_info_menu():
    while True:
        key_info()
        choice = input_output.get_user_input("Enter your choice: ")

        if choice == "1":
            private_key_info()
        elif choice == "2":
            public_key_info()
        
        elif choice == "3":
            break
        elif choice == "4":
            print_color("Exiting the program.", Fore.CYAN)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)
        input("\nPress Enter to proceed or leave idle to exit...")     
            
def private_key_info():
    print("""
    Ownership: The private key is kept secret and known only to the owner.
    
    Usage: It is used for decrypting messages that were encrypted with the corresponding public key.
           It is also used to digitally sign messages or data to verify the sender's identity.
           
    Private Key Security: The security of the entire system relies on keeping the private key confidential.
                          If someone gains access to the private key, they can decrypt messages and forge digital signatures.
    """)

def public_key_info():
    print("""
    Distribution: The public key is openly shared and distributed to anyone who needs it.
    
    Usage: It is used for encrypting messages or data that can only be decrypted by the corresponding private key.
           It is also used to verify the authenticity of digital signatures created with the private key.
           
    Public Key Distribution: Public keys can be freely distributed, and it's computationally infeasible to derive the private key from the public key.
    """)


def private_key_menu():
    while True:
        private_key_page()
        choice = input_output.get_user_input("Enter your choice: ")

        if choice == "1":
            handle_caesar_cipher()
        elif choice == "2":
            handle_substitution_cipher()
        elif choice == "3":
            handle_vigenere_cipher()
        elif choice == "4":
            handle_hill_cipher()
        elif choice == "5":
            handle_homophonic_cipher()
        elif choice == "6":
            cipher_info_menu()
        elif choice == "7":
            break
        elif choice == "8":
            print_color("Exiting the program.", Fore.CYAN)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)

            

def public_key_menu():
    while True:
        public_key_page()
        choice = input_output.get_user_input("Enter your choice: ")

        if choice == "1":
            handle_rsa_encryption()
        elif choice == "2":
            handle_diffie_hellman()
        elif choice == "3":
            cipher_info_menu2()
        elif choice == "4":
            break
        elif choice == "5":
            print_color("Exiting the program.", Fore.CYAN)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)

def cipher_info_menu():
    while True:
        cipher_info_page()
        choice = input_output.get_user_input("Enter your choice: ")

        if choice == "1":
            info = caesar_cipher.caesar_cipher_info()
            input_output.display_output(info)
        elif choice == "2":
            info = substitution_cipher.substitution_cipher_info()
            input_output.display_output(info)
        elif choice == "3":
            info = vigenere_cipher.vigenere_cipher_info()
            input_output.display_output(info)
        
        elif choice == "4":
            info = hill_cipher.hill_cipher_info()
            input_output.display_output(info)
        elif choice == "5":
            info = homophonic.homophonic_cipher_info()
            input_output.display_output(info)
        elif choice == "6":
            break
        elif choice == "7":
            print_color("Exiting the program.", Fore.CYAN)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)
        input("\nPress Enter to proceed or leave idle to exit...")     
            
def cipher_info_menu2():
    while True:
        private_key_info1()
        choice = input_output.get_user_input("Enter your choice: ")

        if choice == "1":
            info = rsa.rsa_info()
            input_output.display_output(info)
        elif choice == "2":
            info = diffie_hellman.diffie_hellman_info()
            input_output.display_output(info)
        
        elif choice == "3":
            break
        elif choice == "4":
            print_color("Exiting the program.", Fore.CYAN)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)   
        input("\nPress Enter to proceed or leave idle to exit...")              
            

def handle_caesar_cipher():
    try:
        while True:
            print_color("\n********************* C4353R CIPH3R *********************", Fore.MAGENTA)
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Info")
            print_color("4. Go Back", Fore.CYAN)
            print_color("5. Exit", Fore.RED)

            caesar_choice = input_output.get_user_input("Enter your choice: ")

            if caesar_choice == "1":
                use_random_shift = input("Use a random shift? (yes/no): ").lower() == "yes"

                if use_random_shift:
                    shift = random.randint(1, 25)
                else:
                    try:
                        shift = int(input("Enter the shift value: "))
                    except ValueError:
                        print_color("Invalid input. Please enter a valid integer for the shift value.", Fore.RED)
                        continue  

                custom_alphabet_option = input("Do you want to use a custom alphabet for encryption? (yes/no): ").lower()
                if custom_alphabet_option == "yes":
                    custom_alphabet = caesar_cipher.generate_custom_alphabet()
                else:
                    custom_alphabet = caesar_cipher.generate_alphabet()
                rounds = int(input("Enter the number of encryption rounds: "))
                message = input("Enter the message: ")

                print_color("\nEncrypting...", Fore.GREEN)
                encrypted_left, encrypted_right = caesar_cipher.encrypt(message, shift, custom_alphabet, rounds)
                print_color(f"\nShift: {shift}", Fore.CYAN)
                print_color(f"\nFinal Encrypted Message (Left Shift): {encrypted_left}", Fore.YELLOW)
                print_color(f"\nFinal Encrypted Message (Right Shift): {encrypted_right}", Fore.YELLOW)

            elif caesar_choice == "2":
                ciphertext = input_output.get_user_input("Enter the ciphertext: ")
                
                custom_alphabet_option = input("Do you want to use a custom alphabet for decryption? (yes/no): ").lower()
                if custom_alphabet_option == "yes":
                    custom_alphabet = caesar_cipher.generate_custom_alphabet()
                else:
                    custom_alphabet = caesar_cipher.generate_alphabet()
                
                print("Choose decryption option:\n1. Known key\n2. Brute-force decryption ")
                option = input_output.get_user_input("\nEnter the option (1/2):")

                if option == "1":
                    key = int(input_output.get_user_input("Enter the key: "))
                    caesar_cipher.decrypt(custom_alphabet, ciphertext, option=1, key_or_word=key)
                elif option == "2":
                    caesar_cipher.decrypt(custom_alphabet, ciphertext, option=2)
                else:
                    display_feedback("Invalid choice. Please try again.", success=False)

            elif caesar_choice == "3":
                info = caesar_cipher.caesar_cipher_info()
                input_output.display_output(info)

            elif caesar_choice == "4":
                break

            elif caesar_choice == "5":
                display_feedback("Exiting the program.", success=True)
                exit()

            else:
                display_feedback("Invalid choice. Please try again.", success=False)
                
            input("\nPress Enter to proceed or leave idle to exit...")     

    except Exception as e:
        print_color(f"An unexpected error occurred: {e}", Fore.RED)
        input("\nPress Enter to proceed or leave idle to exit...") 
       


def handle_substitution_cipher():
    try:
        while True:
            print_color("\n********************* Substitution Cipher *********************", Fore.MAGENTA)
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Info")
            print_color("4. Go Back", Fore.CYAN)
            print_color("5. Exit", Fore.RED)

            substitution_choice = input_output.get_user_input("Enter your choice: ")

            if substitution_choice == "1":
                print("\nEncryption Options:")
                print("1. Enter Key Manually")
                print("2. Generate Random Key")
                print("3. Import Key from File")

                encrypt_option = input_output.get_user_input("Enter encryption option: ")

                if encrypt_option == "1":
                    substitution_key = substitution_cipher.generate_custom_substitution_key()
                elif encrypt_option == "2":
                    substitution_key = substitution_cipher.generate_random_substitution_key()
                    save_key = input("Do you want to save the generated key to a file? (yes/no): ").lower()
                    if save_key == "yes":
                        substitution_cipher.save_substitution_key_to_file(substitution_key)
                elif encrypt_option == "3":
                    file_path = input_output.get_user_input("Enter the file path of the substitution key: ")
                    substitution_key = substitution_cipher.load_substitution_key_from_file(file_path)
                else:
                    display_feedback("Invalid option. Please try again.", success=False)
                    continue

                plaintext = input_output.get_user_input("Enter the plaintext: ")

                

                encrypted_message = substitution_cipher.encrypt_substitution(plaintext, substitution_key)
                print_color(f"\nSubstitution Key: {substitution_key}", Fore.CYAN)
                print_color(f"Encrypted Message: {encrypted_message}", Fore.YELLOW)

            elif substitution_choice == "2":
                print("\nDecryption Options:")
                print("1. Enter Key Manually")
                print("2. Import Key from File")

                decrypt_option = input_output.get_user_input("Enter decryption option: ")

                if decrypt_option == "1":
                    substitution_key = substitution_cipher.generate_custom_substitution_key()
                elif decrypt_option == "2":
                    file_path = input_output.get_user_input("Enter the file path of the substitution key: ")
                    substitution_key = substitution_cipher.load_substitution_key_from_file(file_path)
                else:
                    display_feedback("Invalid option. Please try again.", success=False)
                    continue

                ciphertext = input_output.get_user_input("Enter the ciphertext: ")

                

                decrypted_message = substitution_cipher.decrypt_substitution(ciphertext, substitution_key)
                
                print_color(f"Decrypted Message: {decrypted_message}", Fore.YELLOW)

            elif substitution_choice == "3":
                info = substitution_cipher.substitution_cipher_info()
                input_output.display_output(info)

            elif substitution_choice == "4":
                break

            elif substitution_choice == "5":
                display_feedback("Exiting the program.", success=True)
                exit()

            else:
                display_feedback("Invalid choice. Please try again.", success=False)

            input("\nPress Enter to proceed or leave idle to exit...")
    
    except Exception as e:
        print_color(f"An error occurred: {e}", Fore.RED)
        input("\nPress Enter to proceed or leave idle to exit...")






def handle_diffie_hellman():
    prime = None
    user_private_key = None
    user_public_key = None
    other_public_key = None
    shared_secret_key = None

    while True:
        print_color("\n********************* Welcome to the Diffie-Hellman Key Exchange! *********************", Fore.YELLOW)
        print("\nSelect an option:")
        print("1. Generate your private and public key")
        print("2. Communicate")
        print("3. Calculate shared secret key")
        print("4. Info")
        print_color("5. Go Back", Fore.CYAN)
        print_color("6. Exit", Fore.RED)

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            try:
                user_private_key, user_public_key, prime = D=diffie_hellman.perform_key_exchange()
                print_color(f"\nYour Private Key: {user_private_key}", Fore.GREEN)
                print_color(f"Your Public Key: {user_public_key}", Fore.GREEN)    
            except ValueError as e:
                print_color(f"Error: {e}", Fore.RED)

        elif choice == "2":
                                  print(""" This is the Communication Channel.
                                        Talk to your friend and ask for his public key.
                                        Procedure :
                                        - Open a terminal window and navigate to the directory where server.py and client.py is located.
                                        - Run the command: python server.py
                                        - Open two terminal windows and navigate to the directory where client.py is located.
                                        - In the first terminal, run the command: python client.py
                                        - In the second terminal, run the command: python client.py
                                        - Communicate and share the generated public key with you.
                                        - Continue with step 3 in the main menu to calculate the shared secret key.""")

        elif choice == "3":
            try:
                other_public_key = int(input("Enter the other user's public key: "))
                print_color(f"\nOther User's Public Key: {other_public_key}", Fore.GREEN)
                
                if user_private_key is None or user_public_key is None or other_public_key is None:
                    print_color("Please complete steps 1 and 2 before calculating the shared secret key.", Fore.RED)
                    continue

                shared_secret_key = diffie_hellman.calculate_secret_key(other_public_key, user_private_key, prime)
                print_color(f"\nShared Secret Key: {shared_secret_key}", Fore.GREEN)
            except ValueError as e:
                print_color(f"Error: {e}", Fore.RED)
        elif choice == "4":
            info = diffie_hellman.diffie_hellman_info()
            input_output.display_output(info)

        elif choice == "5":
            break

        elif choice == "6":
            print_color("Exiting the program.", Fore.RED)
            break

        else:
            print_color("Invalid choice. Please try again.", Fore.RED)

        input("\nPress Enter to proceed or leave idle to exit...")

    
def handle_vigenere_cipher():
    while True:
        print_color("\n********************* Welcome to the Vigenère Cipher! *********************", Fore.MAGENTA)
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Info")
        print_color("4. Go Back", Fore.CYAN)
        print_color("5. Exit", Fore.RED)

        choice = input_output.get_user_input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            handle_vigenere_encryption()
        elif choice == "2":
            handle_vigenere_decryption()
        elif choice == "3":
            info = vigenere_cipher.vigenere_cipher_info()
            input_output.display_output(info)
        elif choice == "4":
            break
        elif choice == "5":
            display_feedback("Exiting the program.", success=True)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)

        input("\nPress Enter to proceed or leave idle to exit...")

        

def handle_vigenere_encryption():
    print_color(f"\n********************* Vigenère Cipher - Encryption *********************", Fore.MAGENTA)
    plaintext = input_output.get_user_input("Enter the plaintext: ")

    key_option_detail = input_output.get_user_input(
        "Choose key option:\n1. Manually enter key\n2. Random key\n3. Repeating keyword\nEnter option (1/2/3): ")

    if key_option_detail == "1":
        key = input_output.get_user_input("Enter the key: ")
    elif key_option_detail == "2":
        key = vigenere_cipher.generate_random_key(len(plaintext))
    elif key_option_detail == "3":
        keyword = input_output.get_user_input("Enter the repeating keyword: ")
        key = vigenere_cipher.generate_repeating_keyword(keyword, len(plaintext))
    else:
        display_feedback("Invalid choice. Please try again.", success=False)
        return

    save_key = input_output.get_user_input("Do you want to save the key to a file? (yes/no): ").lower() == "yes"
    if save_key:
        key_filename = input_output.get_user_input("Enter the key file path: ")
        vigenere_cipher.save_key_to_file(key, key_filename)

    ciphertext = vigenere_cipher.encrypt_vigenere(plaintext, key)
    print_color(f"\nKey: {key}", Fore.CYAN)
    print_color(f"\nEncrypted Message: {ciphertext}", Fore.YELLOW)

def handle_vigenere_decryption():
    print_color(f"\n********************* Vigenère Cipher - Decryption *********************", Fore.MAGENTA)

    ciphertext = input_output.get_user_input("Enter the ciphertext: ")

    key_option = input_output.get_user_input("Choose key option:\n1. Manually enter key\n2. Use key from file\nEnter option (1/2): ")

    if key_option == "1":
        key = input_output.get_user_input("Enter the key: ")
    elif key_option == "2":
        key_filename = input_output.get_user_input("Enter the key file path: ")
        key = vigenere_cipher.read_key_from_file(key_filename)
    else:
        display_feedback("Invalid choice. Please try again.", success=False)
        return

    plaintext = vigenere_cipher.decrypt_vigenere(ciphertext, key)
    print_color(f"\nDecrypted Message: {plaintext}", Fore.YELLOW)

     
    

def handle_rsa_encryption():
    while True:
        print_color("\n********************* RSA Encryption *********************", Fore.YELLOW)
        print("Select an option:")
        print("1. Generate RSA key pair")
        print("2. Encrypt message")
        print("3. Decrypt message")
        print("4. Info")
        print_color("5. Go Back", Fore.CYAN)
        print_color("6. Exit", Fore.RED)

        rsa_choice = input_output.get_user_input("Enter your choice (1/2/3/4/5/6): ")

        if rsa_choice == "1":
            bits = int(input_output.get_user_input("Enter the number of bits for key generation: "))
            rsa.validate_bits(bits)
            public_key, private_key = rsa.generate_keypair(bits)
            print_color(f"Public Key: {public_key}", Fore.CYAN)
            print_color(f"Private Key: {private_key}", Fore.CYAN)

            save_choice = input_output.get_user_input("Do you want to save the private key to a file? (yes/no): ")
            if save_choice.lower() == 'yes':
                filename = input_output.get_user_input("Enter the filename: ")
                rsa.save_key_to_file(private_key, filename)
            save_choice1 = input_output.get_user_input("Do you want to save the public key to a file? (yes/no): ")
            if save_choice1.lower() == 'yes':
                filename = input_output.get_user_input("Enter the filename: ")
                rsa.save_key_to_file(public_key, filename)  

        elif rsa_choice == "2":
            message = input_output.get_user_input("Enter the message to encrypt: ")
            rsa.validate_message(message)
            print("Select an option:")
            print("1. Use existing public key")
            print("2. Generate a new public key for the recipient")
            print("3. Import public key from file")
            print_color("4. Go Back", Fore.CYAN)

            encrypt_choice = input_output.get_user_input("Enter your choice: ")

            if encrypt_choice == "1":
                public_key = input_output.get_tuple_input("Enter the recipient's public key (e, n): ")
                rsa.validate_public_key(public_key)
                if public_key is None:
                    continue  

            elif encrypt_choice == "2":
                recipient_bits = int(input_output.get_user_input("Enter the number of bits for the recipient's key generation: "))
                rsa.validate_bits(recipient_bits)
                public_key, private_key = rsa.generate_keypair(recipient_bits)
                print_color(f"Recipient's Public Key: {public_key}", Fore.CYAN)
                print_color(f"Recipient's Private Key: {private_key}", Fore.CYAN)

            elif encrypt_choice == "3":
                filename = input_output.get_user_input("Enter the filename containing the recipient's public key: ")
                try:
                    public_key = rsa.load_key_from_file(filename)
                    rsa.validate_public_key(public_key)
                    
                except FileNotFoundError:
                    display_feedback("File not found. Please enter a valid filename.", success=False)
                    continue  

            elif encrypt_choice == "4":
                continue 

            encrypted_message = rsa.encrypt_message(message, public_key)
            print_color(f"Encrypted Message: {encrypted_message}", Fore.GREEN)

        elif rsa_choice == "3":
            encrypted_message = input_output.get_int_list_input("Enter the encrypted message: ")
            rsa.validate_encrypted_message(encrypted_message)
            print("Select an option:")
            print("1. Use existing private key")
            print("2. Import private key from file")
            print_color("3. Go Back", Fore.CYAN)

            decrypt_choice = input_output.get_user_input("Enter your choice: ")

            if decrypt_choice == "1":
                private_key = input_output.get_tuple_input("Enter your private key (d, n): ")
                rsa.validate_private_key(private_key)
                if private_key is None:
                    continue  

            elif decrypt_choice == "2":
                filename = input_output.get_user_input("Enter the filename containing your private key: ")
                try:
                    private_key = rsa.load_key_from_file(filename)
                    rsa.validate_private_key(private_key)
                except FileNotFoundError:
                    display_feedback("File not found. Please enter a valid filename.", success=False)
                    continue  

            elif decrypt_choice == "3":
                continue  

            decrypted_message = rsa.decrypt_message((encrypted_message), (private_key))
            print_color(f"Decrypted Message: {decrypted_message}", Fore.GREEN)

        elif rsa_choice == "4":
            info = rsa.rsa_info()
            input_output.display_output(info)
        elif rsa_choice == "5":
            break
        elif rsa_choice == "6":
            display_feedback("Exiting the program.", success=True)
            exit()
        else:
            display_feedback("Invalid choice. Please try again.", success=False)

        input("\nPress Enter to proceed or leave idle to exit...")

  

def handle_hill_cipher():
    while True:
        print_color("\n********************* Hill Cipher *********************", Fore.YELLOW)
        print("Choose an option:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Info about Hill Cipher")
        print_color("4. Go Back", Fore.CYAN)
        print_color("5. Exit", Fore.RED)

        option = input_output.get_user_input("Enter the option number (1/2/3/4/5): ")
        

        if option == '1':
            encrypt_menu()
        elif option == '2':
            decrypt_menu()
        elif option == '3':
            hill_cipher.hill_cipher_info()
        elif option == '4':
            break
        elif option == '5':
            print_color("Exiting the program.", Fore.RED)
            exit()
        else:
            display_feedback("Invalid option. Please choose a valid option.", success=False)

        input("\nPress Enter to proceed or leave idle to exit...")

def encrypt_menu():
    print_color("\n********************* Hill Cipher - Encrypt *********************", Fore.YELLOW)
    alphabet = string.ascii_uppercase + string.digits
    key_matrix = hill_cipher.enter_key_manually(alphabet)
    hc = hill_cipher.HillCipher(numpy.array(key_matrix))
    text_e = input("ENTER PLAIN TEXT : ")
    print_color(f"\nOriginal message: {text_e}", Fore.CYAN)
    print_color("Your encrypted text is:", Fore.GREEN)
    print(hc.encrypt(text_e))
    
    

def decrypt_menu():
    print_color("\n********************* Hill Cipher - Decrypt *********************", Fore.YELLOW)
    alphabet = string.ascii_uppercase + string.digits
    key_matrix = hill_cipher.enter_key_manually(alphabet)
    hc = hill_cipher.HillCipher(numpy.array(key_matrix))
    text_d = input("CIPHER TEXT : ")
    print_color(f"\nEncrypted message: {text_d}", Fore.CYAN)
    print_color("Your decrypted text is:", Fore.GREEN)
    print(hc.decrypt(text_d))
 

def handle_homophonic_cipher():
    while True:
        print_color("\n********************* Homophonic Cipher *********************", Fore.MAGENTA)
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Info")
        print_color("4. Go Back", Fore.CYAN)
        print_color("5. Exit", Fore.RED)

        homophonic_choice = input_output.get_user_input("Enter your choice (1/2/3/4): ")

        if homophonic_choice == "1":
            handle_homophonic_encrypt()

        elif homophonic_choice == "2":
            handle_homophonic_decrypt()

        elif homophonic_choice == "3":
            info = homophonic.homophonic_cipher_info()
            input_output.display_output(info)

        elif homophonic_choice == "4":
            break
        
        elif homophonic_choice == '5':
            print_color("Exiting the program.", Fore.RED)
            exit()

        else:
            display_feedback("Invalid choice. Please try again.", success=False)

        input("\nPress Enter to proceed or leave idle to exit...")

def handle_homophonic_encrypt():
    print_color("\n********************* Homophonic Cipher - Encryption *********************", Fore.MAGENTA)
    plaintext = input_output.get_user_input("Enter the plaintext: (CAN USE A-Z , a-z , 0-9 and Special Characters) ")

    key_option = input_output.get_user_input(
        "Choose key option:\n1. Manually enter key\n2. Random key\n3. Import key from file\nEnter option (1/2/3): ")

    if key_option == "1":
        homophonic_key = homophonic.handle_manual_key_entry()
    elif key_option == "2":
        homophonic_key = homophonic.generate_homophonic_key()
        save_key = input_output.get_user_input("Do you want to save the key to a file? (yes/no): ").lower() == "yes"
        if save_key:
            key_filename = input_output.get_user_input("Enter the key file path: ")
            homophonic.save_homophonic_key_to_file(homophonic_key, key_filename)
    elif key_option == "3":
        key_filename = input_output.get_user_input("Enter the key file path: ")
        homophonic_key = homophonic.load_homophonic_key_from_file(key_filename)
    else:
        display_feedback("Invalid choice. Please try again.", success=False)
        return

    ciphertext = homophonic.encrypt_homophonic(plaintext, homophonic_key)
    print_color(f"\nHomophonic Key: {homophonic_key}", Fore.CYAN)
    print_color(f"\nEncrypted Message: {ciphertext}", Fore.GREEN)

def handle_homophonic_decrypt():
    print_color("\n********************* Homophonic Cipher - Decryption *********************", Fore.MAGENTA)
    ciphertext = input_output.get_user_input("Enter the ciphertext: ")

    key_option = input_output.get_user_input(
        "Choose key option:\n1. Manually enter key\n2. Import key from file\nEnter option (1/2): ")

    if key_option == "1":
        homophonic_key = homophonic.handle_manual_key_entry()
    elif key_option == "2":
        key_filename = input_output.get_user_input("Enter the key file path: ")
        homophonic_key = homophonic.load_homophonic_key_from_file(key_filename)
    else:
        display_feedback("Invalid choice. Please try again.", success=False)
        return

    plaintext = homophonic.decrypt_homophonic(ciphertext, homophonic_key)
    print_color(f"\nDecrypted Message: {plaintext}", Fore.GREEN)





if __name__ == "__main__":
    main()
        




