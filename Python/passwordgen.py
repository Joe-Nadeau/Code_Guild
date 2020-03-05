# PDX Code Guild
# Lab 6
# Random password generator


# import random
# import string

# lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
# uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# special_character = '!@#$%^&*'

# pass_length = input('Enter desired number of characters for you password: ')
# pass_length = int(pass_length)


# x = 0
# new_password =[]

# while x < pass_length :
#     rand_selecter = [random.choice(lowercase_letter), random.choice(uppercase_letter), random.choice(number), random.choice(special_character)]
#     print(random.choice(rand_selecter), end='')

#     x += 1

import random
import string

def password_picker(lc_count, uc_count, dig_count, spec_count, password):
    for i in range(0, lc_count):
        password.append(random.choice(string.ascii_lowercase))
    for i in range(0, uc_count):
        password.append(random.choice(string.ascii_uppercase))
    for i in range(0, dig_count):
        password.append(random.choice(string.digits))
    for i in range(0, spec_count):
        password.append(random.choice(string.punctuation))
    random.shuffle(password)
    passtring = ''.join(password)
    print(passtring)

def main():
    
    password = []

    print('Let\'s work together to create a secure password for you')
    lc_count = int(input('How many lowercase characters would you like in your password? '))
    uc_count = int(input('How many uppercase characters would you like in your password? '))
    dig_count = int(input('How many numbers would you like in your password? '))
    spec_count =int(input('How many special characters would you like in your password? '))
    
    password_picker(lc_count, uc_count, dig_count, spec_count, password)
    
main()
