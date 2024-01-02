import numpy
import string
from colorama import Fore, Style

def greatest_common_divisor(a: int, b: int) -> int:
    return b if a == 0 else greatest_common_divisor(b % a, a)

def print_color(message, color):
    print(color + message + Style.RESET_ALL)

class HillCipher:
    key_string = string.ascii_uppercase + string.digits
    modulus = numpy.vectorize(lambda x: x % 36 )

    to_int = numpy.vectorize(lambda x: round(x) )

    def __init__(self, encrypt_key):
    
        self.encrypt_key = numpy.array(encrypt_key) if not isinstance(encrypt_key, numpy.ndarray) else encrypt_key
        self.check_determinant()
        self.decrypt_key = None
        self.break_key = self.encrypt_key.shape[0]

    def replace_letters(self, letter: str) -> int:
        return self.key_string.index(letter)

    def replace_digits(self, num: int) -> str:
        return self.key_string[round(num)]

    def check_determinant(self) -> None:
        det = round(numpy.linalg.det(self.encrypt_key))
        if det < 0:
            det = det % len(self.key_string)
        req_l = len(self.key_string)
        if greatest_common_divisor(det, len(self.key_string)) != 1:
            raise ValueError(
                f"determinant modular {req_l} of encryption key({det}) is not co prime w.r.t {req_l}.\nTry another key."
            )

    def process_text(self, text: str) -> str:
        chars = [char for char in text.upper() if char in self.key_string]
        last = chars[-1]
        while len(chars) % self.break_key != 0:
            chars.append(last)
        return "".join(chars)


    def encrypt(self, message: str) -> str:
        message = self.process_text(message.upper())
        encrypted = ""

        for i in range(0, len(message) - self.break_key + 1, self.break_key):
            batch = message[i : i + self.break_key]
            batch_vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([batch_vec]).T
            batch_encrypted = self.modulus(self.encrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            encrypted_batch = "".join(
                self.replace_digits(num) for num in batch_encrypted
            )
            encrypted += encrypted_batch

        return encrypted

    def make_decrypt_key(self):
        det = round(numpy.linalg.det(self.encrypt_key))
        if det < 0:
            det = det % len(self.key_string)
        det_inv = None
        for i in range(len(self.key_string)):
            if (det * i) % len(self.key_string) == 1:
                det_inv = i
                break
        inv_key = (
            det_inv
            * numpy.linalg.det(self.encrypt_key)
            * numpy.linalg.inv(self.encrypt_key)
        )
        return self.to_int(self.modulus(inv_key))

    def decrypt(self, message: str) -> str:
        self.decrypt_key = self.make_decrypt_key()
        message = self.process_text(message.upper())
        decrypted = ""

        for i in range(0, len(message) - self.break_key + 1, self.break_key):
            batch = message[i : i + self.break_key]
            batch_vec = [self.replace_letters(char) for char in batch]
            batch_vec = numpy.array([batch_vec]).T
            batch_decrypted = self.modulus(self.decrypt_key.dot(batch_vec)).T.tolist()[
                0
            ]
            decrypted_batch = "".join(
                self.replace_digits(num) for num in batch_decrypted
            )
            decrypted += decrypted_batch

        return decrypted



def enter_key_manually(alphabet):
    try:
        
        print(f"Note: Enter space-separated values for each row, and press Enter after each row. Use only A-Z AND 0-9")
        try:
            N = int(input("Enter the order of the key matrix (N): "))
        except ValueError:
            print_color("Invalid input. Please enter a valid integer for the shift value.", Fore.RED)
            SystemExit
        key_matrix = []

        for i in range(N):
            row = input(f"Enter values for row {i + 1} (space-separated): ").split()
            if len(row) != N:
                raise ValueError(f"Invalid number of elements. Please enter {N} elements.")
            key_matrix.append([int(val) for val in row])

        return (key_matrix)
    except ValueError as e:
        print_color(f"Error: {e}", Fore.RED)

