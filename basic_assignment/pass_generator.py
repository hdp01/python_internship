import random

string_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_num = '0123456789'
string_special = '~!@#$%^&*()'

def generate_password(length, use_special_chars, use_numbers):
    password = ''

    for _ in range(length-2):
        password += random.choice(string_char)

    if use_numbers:
        password = password + random.choice(string_num)
    else:
        password = password + random.choice(string_char)

    if use_special_chars:
        password = password + random.choice(string_special)
    else:
        password = password + random.choice(string_char)

    return password

length = int(input("Enter the length of the password: "))
use_special_chars = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'
use_numbers = input("Do you want to include numbers? (yes/no): ").lower() == 'yes'

generated_password = generate_password(length, use_special_chars, use_numbers)
print("\n")
print("Generated Password:", generated_password)