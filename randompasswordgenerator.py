# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:54:43 2023

@author: pulig
"""

import random
import string
import sys

def generate_strong_password(length):

    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation


    password = (
        random.choice(uppercase_letters)
        + random.choice(lowercase_letters)
        + random.choice(digits)
        + random.choice(special_characters)
    )


    remaining_length = length - 4
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += ''.join(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the characters to randomize the password
    password_list = list(password)
    random.shuffle(password_list)
    final_password = ''.join(password_list)

    return final_password

if __name__=="__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    n = int(sys.argv[1])
    password = generate_strong_password(n)
    print("Password:", password)