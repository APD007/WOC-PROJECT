import random
import math
from colorama import Fore, Style
from sympy import randprime

def print_color(text, color=Fore.WHITE):
    print(color + text + Style.RESET_ALL)

def generate_keypair(bits):
    try:
        validate_bits(bits)
        p, q = generate_primes(bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = choose_public_key(phi)
        d = calculate_private_key(e, phi)
        public_key = (e, n)
        private_key = (d, n)
        return public_key, private_key
    except ValueError as e:
        print_color(f"Error: {e}", Fore.RED)

def generate_primes(bits):
    p = randprime(2**(bits-1), 2**bits - 1)
    q = randprime(2**(bits-1), 2**bits - 1)
    return p, q

def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if num == 2:
            return num
        if num % 2 != 0 and is_prime(num):
            return num

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def choose_public_key(phi):
    while True:
        e = random.randint(2, phi - 1)
        if math.gcd(e, phi) == 1:
            return e

def calculate_private_key(e, phi):
    d = modular_inverse(e, phi)
    return d

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt_message(message, public_key):
    try:
        validate_message(message)
        validate_public_key(public_key)
        e, n = public_key
        encrypted_message = [pow(ord(char), e, n) for char in message]
        return encrypted_message
    except ValueError as e:
        print_color(f"Error: {e}", Fore.RED)

def decrypt_message(encrypted_message, private_key):
    try:
        validate_encrypted_message(encrypted_message)
        validate_private_key(private_key)
        d, n = private_key
        decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
        return ''.join(decrypted_message)
    except ValueError as e:
        print_color(f"Error: {e}", Fore.RED)

def rsa_info():
    info = """
    RSA (Rivest–Shamir–Adleman) Encryption

    RSA is a widely used public-key cryptosystem that enables secure data transmission.
    It is named after its inventors Ron Rivest, Adi Shamir, and Leonard Adleman.

    Key Generation:
    - Two large prime numbers, p and q, are selected.
    - The modulus n is calculated as n = p * q.
    - The totient (phi) is computed as phi = (p - 1) * (q - 1).
    - A public exponent e is chosen, typically 65537.
    - The private exponent d is computed as the modular inverse of e modulo phi.
    - Public key: (e, n)
    - Private key: (d, n)

    Encryption:
    - Convert the plaintext message to numerical values.
    - Apply the public exponent and modulus using modular exponentiation.

    Decryption:
    - Apply the private exponent and modulus using modular exponentiation.

    Security:
    - RSA security relies on the difficulty of factoring large composite numbers.
    - Breaking RSA involves factoring the modulus n, which becomes computationally infeasible for large primes.
    - Key length is crucial; longer keys provide higher security but demand more computation.
    - Common key lengths are 2048 and 3072 bits.

    Note: This simplified implementation may not cover all security considerations.
    """
    return info


def save_key_to_file(key, filename):
    try:
        with open(filename, 'w') as file:
            file.write(str(key))
        print_color(f"Key saved to {filename}", Fore.GREEN)
    except Exception as e:
        print_color(f"Error saving key: {e}", Fore.RED)


def load_key_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return eval(file.read())
    except FileNotFoundError:
        print_color("File not found. Please check the file path and try again.", Fore.RED)
    except Exception as e:
        print_color(f"Error loading key: {e}", Fore.RED)


def validate_public_key(key):
    if not isinstance(key, tuple) or len(key) != 2:
        raise ValueError("Invalid public key format. It should be a tuple (e, n).")
    e, n = key
    if not isinstance(e, int) or not isinstance(n, int) or e < 2 or n < 2:
        raise ValueError("Invalid values in the public key (e, n).")


def validate_private_key(key):
    if not isinstance(key, tuple) or len(key) != 2:
        raise ValueError("Invalid private key format. It should be a tuple (d, n).")
    d, n = key
    if not isinstance(d, int) or not isinstance(n, int) or d < 2 or n < 2:
        raise ValueError("Invalid values in the private key (d, n).")


def validate_message(message):
    if not isinstance(message, str):
        raise ValueError("Message should be a string.")


def validate_encrypted_message(encrypted_message):
    if not isinstance(encrypted_message, list) or not all(isinstance(char, int) for char in encrypted_message):
        raise ValueError("Invalid encrypted message format. It should be a list of integers.")

def validate_bits(bits):
    if not isinstance(bits, int) or bits < 4:
        raise ValueError("Key size should be at least 4 bits.")
    elif bits % 2 != 0:
        raise ValueError("Key size should be an even number.")
