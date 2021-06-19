# Exercise 16 - Password Generator

import random
import string

STRONG = 1
MEDIUM = 2
WEAK = 3


def generate_password(password_complexity):
    password_sequence = string.ascii_letters + string.digits + string.punctuation
    if password_complexity == STRONG:
        password = ''.join(random.choice(password_sequence) for i in range(32))
    elif password_complexity == MEDIUM:
        password = ''.join(random.choice(password_sequence) for i in range(16))
    elif password_complexity == WEAK:
        password = ''.join(random.choice(password_sequence) for i in range(8))
    else:
        password = ''

    return password


if __name__ == '__main__':
    print('The choices of password complexity are \n 1. Strong \n 2. Medium \n 3. Weak')
    complexity = int(input('Enter your password complexity choice: '))
    print('Your password is : ', generate_password(complexity))
