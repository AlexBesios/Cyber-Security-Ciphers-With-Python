import numpy as np
from egcd import egcd
import string

alphabet = "abcdefghijklmnopqrstuvwxyz "
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result


def vigenere_cipher(text, key):
    result = ""
    key_length = len(key)
    key_index = 0
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shift = ord(key[key_index % key_length].upper()) - 65
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            key_index += 1
        elif char.isspace():
            result += char
        else:
            result += char
    return result


def affine_cipher(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((a * (ord(char) - ascii_offset) + b) % 26 + ascii_offset)
        else:
            result += char
    return result


def matrix_mod_inv(matrix, modulus):  # for HILL cipher
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    ) % modulus

    return matrix_modulus_inv


def hill_cipher(text, key_matrix):
    result = ""
    result_in_numbers = []

    # results into numbers
    for letter in text:
        result_in_numbers.append(letter_to_index[letter])

    # split the result into the size of key matrix
    split_text = [
        result_in_numbers[i : i + int(key_matrix.shape[0])]
        for i in range(0, len(result_in_numbers), int(key_matrix.shape[0]))
    ]

    # encrypt couples of letters
    for text in split_text:
        text = np.transpose(np.asarray(text))[:, np.newaxis]

        while text.shape[0] != key_matrix.shape[0]:
            text = np.append(text, letter_to_index["x"])[:, np.newaxis]

        numbers = np.dot(key_matrix, text) % 27

        n = numbers.shape[0]

        # convert numbers to letters
        for idx in range(n):
            number = int(numbers[idx, 0])
            result += index_to_letter[number]

    return result


def substitution_cipher(text, dictionary):
    return "".join(dictionary.get(char, char) for char in text)


def otp_cipher(text, key):
    cipher_text = ""

    cipher = []
    for i in range(len(key)):
        cipher.append(ord(text[i]) - ord("A") + ord(key[i]) - ord("A"))

    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26

    for i in range(len(key)):
        x = cipher[i] + ord("A")
        cipher_text += chr(x)

    return cipher_text


def is_prime(num):  # for RSA cipher
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def rsa_cipher(text, p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    return [pow(ord(char), e, n) for char in text]


while True:
    cipher_type = input(
        "Give the type of cipher you want to use (Available options are Caesar, Vigenere, Affine, HILL, Substitution, OTP, RSA or stop to exit the program):\n"
    )

    if cipher_type == "Caesar":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the Caesar cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    print("Give text and shift value")
                    text = input()
                    shift = int(input())
                    confirm_data = input(
                        "Are you sure you want to use Caesar cipher with text: "
                        + text
                        + " and shift value: "
                        + str(shift)
                        + "? (yes/no)\n"
                    )
                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                print("Result: " + caesar_cipher(text, shift))
                break
            else:
                print("Wrong answer, please try again\n")

    elif cipher_type == "Vigenere":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the Vigenere cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    print("Give text and key")
                    text = input()
                    key = input()
                    confirm_data = input(
                        "Are you sure you want to use Vigenere cipher with text: "
                        + text
                        + " and key value: "
                        + key
                        + "? (yes/no)\n"
                    )
                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                print("Result: " + vigenere_cipher(text, key))
                break
            else:
                print("Wrong answer, please try again\n")

    elif cipher_type == "Affine":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the Affine cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    print("Give text and a, b values")
                    text = input()
                    a = int(input())
                    b = int(input())
                    confirm_data = input(
                        "Are you sure you want to use Affine cipher with text: "
                        + text
                        + " and a, b values: "
                        + str(a)
                        + ", "
                        + str(b)
                        + "? (yes/no)\n"
                    )
                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                print("Result: " + affine_cipher(text, a, b))
                break

    elif cipher_type == "HILL":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the HILL cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    text = input("Give text (in lower case): ")

                    # ask for matrix size
                    matrix_size = int(
                        input("Enter the number of rows and columns of the matrix: ")
                    )

                    key_matrix = []

                    for i in range(matrix_size):
                        row = []
                        for j in range(matrix_size):
                            row.append(
                                int(
                                    input(f"Enter integer at position ({i+1}, {j+1}): ")
                                )
                            )
                        key_matrix.append(row)

                    print("Matrix: ")
                    for row in key_matrix:
                        print(row)

                    confirm_data = input(
                        "Are you sure you want to use HILL cipher with the text and matrix that you provided? (yes/no)\n"
                    )

                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                key_matrix = np.array(key_matrix)
                print("Result: " + hill_cipher(text, key_matrix))
                break

    elif cipher_type == "Substitution":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the Substitution cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    text = input("Give text: ")

                    print(
                        "Enter a list of letters for the dictionary you want to use, without any spaces:"
                    )
                    letters = list(input())

                    if len(letters) != 26:
                        print("Error: You must enter exactly 26 letters.")
                    else:
                        dictionary = dict(zip(string.ascii_lowercase, letters))

                    confirm_data = input(
                        "Are you sure you want to use Substitution cipher with the text and dictionary you provided? (yes/no)\n"
                    )
                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                print("Result: " + substitution_cipher(text, dictionary))
                break

    elif cipher_type == "OTP":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the OTP cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    text = input("Give text: ")
                    key = input("Give string key: ")

                    if len(key) != len(text):
                        print(
                            "Error: You must enter the same amount of letters as the text."
                        )
                        continue

                    confirm_data = input(
                        "Are you sure you want to use OTP cipher with the text and key you provided? (yes/no)\n"
                    )
                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                print("Result: " + otp_cipher(text.upper(), key.upper()))
                break

    elif cipher_type == "RSA":

        while True:
            confirm_cipher = input(
                "Are you sure you want to use the RSA cipher? (yes/no)\n"
            )
            if confirm_cipher == "no":
                break
            elif confirm_cipher == "yes":

                while True:
                    print("Give text (in lower case) and p, q, e values (integers)")
                    text = input()
                    p = int(input())
                    q = int(input())
                    e = int(input())

                    if not is_prime(p) or not is_prime(q):
                        print("Error: p and q must be prime numbers")
                        continue

                    confirm_data = input(
                        "Are you sure you want to use RSA cipher with text: "
                        + text
                        + " and p, q, e values: "
                        + str(p)
                        + ", "
                        + str(q)
                        + ", "
                        + str(e)
                        + "? (yes/no)\n"
                    )
                    if confirm_data == "yes":
                        break
                    elif confirm_data == "no":
                        continue
                    else:
                        print("Wrong answer, please try again\n")

                print("Result: ", rsa_cipher(text, p, q, e))
                break

    elif cipher_type == "stop":

        break

    else:

        print("Invalid cipher type")
