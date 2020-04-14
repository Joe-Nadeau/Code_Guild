# PDX Code Guild
# Lab 23
# Contact List
# Joey Nadeau

import csv

def new_contact(contacts):
    
    name = input("Enter a name: \n")
    fruit = input("Enter a fruit: \n")
    color = input("Enter a color: \n")
    new_contact = {name: name, favorite_fruit: fruit, favorite_color: color}
    new_contact.append(name)
    new_contact.append(fruit)
    new_contact.append(color)
    contacts.append(new_contact)
    return contacts


def main():

    with open('contacts.csv', 'r') as file:
        #lines = file.read().split('\n')
        reader = csv.reader(file, skipinitialspace = True)
        header = next(reader)
        contacts = [dict(zip(header, map(str, row))) for row in reader]
        #new_contact(contacts)
        print(contacts)

main()

