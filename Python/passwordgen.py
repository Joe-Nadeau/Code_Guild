# PDX Code Guild
# Lab 6
# Random password generator


import random

lowercase_letter = "abcdefghijklmnopqrstuvwxyz"
uppercase_letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_character = '!@#$%^&*'
rand_selecter = [random.choice(lowercase_letter), random.choice(uppercase_letter), random.choice(number), random.choice(special_character)]

x = 0

while x < 12:
    print(random.choice(rand_selecter), end='')
    x += 1

