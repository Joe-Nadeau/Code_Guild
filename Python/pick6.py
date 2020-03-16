#PDX Code Guild
#Lab 14
#Pick 6
#Joey Nadeau



# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance

import random

def pick6():
    num_list = []
    for i in range (6):
        num_list.append(random.randrange(0, 99))
    print(num_list)

def num_matches(winner, ticket):

    match = 0

    for i in winner:
        
        if i in winner == i in ticket:
            match += 1
        else:
            match = match
        return match

def main():

    balance = 0
    winner = pick6()
    ticket = pick6()

    num_matches(winner, ticket)
    print(winner)
    print(ticket)
    print(num_matches)
    

main()