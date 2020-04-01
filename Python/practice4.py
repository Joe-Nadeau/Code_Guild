# PDX Code Guild
# Practice 4: 
# Joey Nadeau

# Problem 1
# Given a the two lists below, combine them into a dictionary.

fruits = ['apple', 'banana', 'pear']
price = [1.2, 3.3, 2.1]

def combine(a, b):
    my_dict = dict(zip(a, b))
    return my_dict
    
print(combine(fruits, price))
