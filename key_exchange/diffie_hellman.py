import random
from colorama import Fore, Style
from sympy import randprime

def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def perform_key_exchange():
    try:
        print_color("\n********************* Welcome to the Diffie-Hellman Key Exchange! *********************", Fore.YELLOW)

        while True:
            print_color("\nSelect an option:", Fore.CYAN)
            print("1. Enter prime number and primitive root manually")
            print("2. Select RANDOMLY")
            print("3. Find possible primitive roots for a given prime")
            print("4. Exit")

            choice = input("Enter your choice (1/2/3/4): ")
            if choice == "1":
                P, G = get_p_and_g_input()
                private_key = generate_private_key(P)
                public_key = calculate_public_key(G, private_key, P)
                print_color(f"\nUser - Private Key: {private_key}, Public Key: {public_key}", Fore.GREEN)

            elif choice == "2":
                P, G = generate_prime_and_primitive_root()
                private_key = generate_private_key(P)
                public_key = calculate_public_key(G, private_key, P)
                print_color(f"\nUser - Private Key: {private_key}, Public Key: {public_key}", Fore.GREEN)

            elif choice == "3":
                P = get_prime_input()
                print_color(f"Possible primitive roots for {P}:", Fore.YELLOW)
                for i in range(2, P):
                    if primitive_check(i, P) == 1:
                        print(i)

                G = get_primitive_root_input(P)
                private_key = generate_private_key(P)
                public_key = calculate_public_key(G, private_key, P)
                print_color(f"\nUser - Private Key: {private_key}, Public Key: {public_key}", Fore.GREEN)

            elif choice == "4":
                print_color("Exiting the program.", Fore.RED)
                break

            else:
                print_color("Invalid choice. Please try again.", Fore.RED)
            return private_key, public_key, P
    except ValueError as e:
        print_color(f"Error: {e}", Fore.RED)

def generate_prime(bits):
    while True:
        num = randprime(2**(bits-1), 2**bits - 1)
        if num % 2 != 0 and is_prime(num):
            return num

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def power_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result

def primitive_check(g, p):
    if not is_prime(p):
        return -1

    phi_p = p - 1
    factors = [2]  
    q = phi_p // 2
    for i in range(3, int(q**0.5) + 1, 2):
        if q % i == 0:
            factors.append(i)
            while q % i == 0:
                q //= i

    if q > 1:
        factors.append(q)

    for factor in factors:
        if power_mod(g, phi_p // factor, p) == 1:
            return -1

    return 1

def generate_private_key(limit):
    try:
        private_key = int(input(f"Enter a private key less than {limit} : "))
        if(private_key < limit):
            return private_key
        else:
            return  print_color("Not a valid Integer.",Fore.RED)
            generate_private_key(limit)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

def calculate_public_key(primitive_root, private_key, prime):
    return pow(primitive_root, private_key, prime)

def calculate_secret_key(other_public_key, private_key, prime):
    return pow(other_public_key, private_key, prime)

def generate_prime_and_primitive_root():
    try:
        bits = int(input("Enter the number of bits for key generation: "))
        validate_bits(bits)

        prime = generate_prime(bits)
        while True:
            primitive_root = random.randint(2, prime - 1)
            if primitive_check(primitive_root, prime) == 1:
                break

        print_color("Randomly selected options:", Fore.YELLOW)
        print_color(f"PRIME NUMBER (P) = {prime}, PRIMITIVE ROOT (G) = {primitive_root}", Fore.YELLOW)

        return prime, primitive_root
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

def get_user_input(prompt):
    return input(prompt)

def validate_bits(bits):
    if not isinstance(bits, int) or bits < 4:
        raise ValueError("Key size should be at least 4 bits.")
    elif bits % 2 != 0:
        raise ValueError("Key size should be an even number.")

def get_p_and_g_input():
    try:
        P = int(input(f"Enter a prime number (P) : "))
        G = int(input(f"Enter a primitive root (G) : "))

        validate_prime_and_primitive_root(P, G)
        return P, G
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

def get_prime_input():
    try:
        P = int(input("Enter a prime number (P): "))
        validate_prime(P)
        return P
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

def get_primitive_root_input(P):
    try:
        G = int(input(f"Enter a primitive root (G) for the given prime number (P = {P}): "))
        validate_primitive_root(G, P)
        return G
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid integer.")

def validate_prime_and_primitive_root(P, G):
    validate_prime(P)
    validate_primitive_root(G, P)

def validate_prime(P):
    if not is_prime(P):
        raise ValueError(f"{P} is not a prime number. Please enter a prime number.")

def validate_primitive_root(G, P):
    if primitive_check(G, P) != 1:
        raise ValueError(f"{G} is not a primitive root for {P}. Please enter a valid primitive root.")



def diffie_hellman_info():
    
    print_color("\n********************* Diffie-Hellman Key Exchange Information *********************", Fore.YELLOW)
    print(f"""

    The Diffie-Hellman key exchange is a method for two parties to establish a shared secret key over an untrusted network.
    The security of the Diffie-Hellman key exchange relies on the difficulty of the discrete logarithm problem.

    Encryption Procedure:
    1. Both parties agree on a large prime number (p) and a primitive root modulo p (g).
    2. Each party privately chooses a random number (a and b, respectively).
    3. They each calculate a public key using (A = g^a mod p) and (B = g^b mod p).
    4. They exchange public keys (A and B).
    5. Both parties independently calculate the shared secret key using the received public key and their own private key.

    Decryption Procedure:
    Diffie-Hellman itself is not used for encryption or decryption. Instead, it's used to establish a shared secret key.
    The shared secret key can then be used with a symmetric-key encryption algorithm for secure communication.

    Security Levels:
    The security of Diffie-Hellman depends on the size of the prime number (p) used. Larger prime numbers provide higher security.
    Commonly used key lengths are 2048, 3072, and 4096 bits. The choice of key length depends on the desired level of security.
    It's important to choose a key length that provides sufficient security for the specific application and the expected lifetime of the key.
    """)
    print_color("\nNote: Diffie-Hellman provides key exchange and not encryption itself. It is often combined with symmetric-key encryption for secure communication.", Fore.CYAN)

