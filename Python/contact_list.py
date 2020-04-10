# PDX Code Guild
# Lab 23
# Contact List
# Joey Nadeau

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)