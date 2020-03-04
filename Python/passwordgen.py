# PDX Code Guild
# Lab 6
# Random password generator


import random

lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_character = '!@#$%^&*'

x = 0
new_password =[]

while x < 12:
    rand_selecter = [random.choice(lowercase_letter), random.choice(uppercase_letter), random.choice(number), random.choice(special_character)]
    # character = random.choice(rand_selecter)
    # rand_selecter.remove(character)
    # new_password.append(character)
    print(random.choice(rand_selecter), end='')

    x += 1

# print("".join(rand_selecter))