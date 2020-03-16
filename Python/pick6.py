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
    return num_list

def num_matches(winner, ticket):

    matches = 0

    for i in winner:
        
        if i in winner == i in ticket:
            matches += 1
        else:
            matches = matches
        return matches
        print(f'There were {matches} matching numbers.'

def balance_tracker(num_matches(winner, ticket)):
    balance = 0

    if match == 0:
        balance = balance - 2
    elif match == 1:
        balance = (balance + 4) - 2
    elif match == 2:
        balance = (balance + 7)- 2
    elif match == 3:
        balance = (balance + 100) - 2
    elif match ==4:
        balance = (balance + 50000) - 2
    elif match == 5:
        balance = (balance + 1000000) - 2
    elif match == 6:
        blance = (balance + 25000000) - 2
    return balance


def main():
    final_balance = 0
    x = 0
    while x < 100:
       
        winner = pick6()
        print(f'The winning numbers are: {winner}')
        ticket = pick6()
        print(f'Your ticket numbers were: {ticket}')
        num_matches(winner, ticket)
        final_balance = final_balance + balance_tracker(match)
        x += 1
    print(f'Your final balance is: ${final_balance}')

main()