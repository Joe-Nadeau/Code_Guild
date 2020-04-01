# PDX Code Guild
# Practice 3: Lists
# Joey Nadeau

# Problem 1
#Write a function using random.randint to generate an index, use that index to pick a random element of a list and return it.

import random

def random_element():

    fruits = ['apples', 'bananas', 'pears', 'cherries', 'starfruit', 'watermelons', 'grapes']
    rand_index = random.randint(0, len(fruits)-1)
    random_word = fruits[rand_index]
    return random_word

#print(random_element())

# Problem 2
#Write a REPL which asks users for a list of numbers, which they enter, until they say 'done'. Then print out the list.

num_list = []

def user_gen_numlist(num_list):
    num_list = []
    user_input = ''
    while user_input != 'done':
        user_input = input('Enter a number (or \'done\'): ')
        if user_input != 'done':
            num_list.append(user_input)
        else:
            continue
    return num_list

# print(user_gen_numlist(num_list))

# Problem 3
#Write a function that takes a list of numbers, and returns True if there is an even number of even numbers.

# list_O_numbers = []
# l = int(input('Enter the number of elements you want to be in the list: '))

# for i in range(0, l):
#     numbs = int(input('Enter a number: '))
#     list_O_numbers.append(numbs)   

# def eveneven(list_O_numbers):
#     even_list = []

#     for i in list_O_numbers:
#         if i % 2 == 0:
#             even_list.append(i)
#         else:
#             even_list = even_list

#     if len(even_list) % 2 == 0:
#         return True
#     else:
#         return False

# print(eveneven(list_O_numbers))

# Problem 4
# Print out every other element of a list, first using a while loop, then using a for loop.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_every_other(nums):
    i = 0
    while i in range(0, len(nums), 2):
        print(nums[i])
        i += 2

#     for i in range(0, len(nums)):
#         if i % 2 == 0:
#             print(i)
    
       
print_every_other(nums)

