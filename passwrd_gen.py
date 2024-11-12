import random
import string


def generatepassword(length):
    letters = string.ascii_letters
    digits = string.digits
    special_xters = string.punctuation

    characters = letters + digits + special_xters

    password = " "
    for _ in range(length):
         password += random.choice(characters)
    return password

def main():
    input_length = eval(input("Enter length of password: "))
    generated_pass = generatepassword(input_length)
    print("Your passsword is: ", generated_pass)

if __name__ == "__main__":
    main()
