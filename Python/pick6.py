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

#Version 2

import random

def pick6():
    num_list = []
    for i in range (6):
        num_list.append(random.randrange(0, 99))
    return num_list

def num_matches(winner, ticket):

    matches = 0

    for i in range(len(winner)):
        
        if ticket[i] == winner[i]:
            matches += 1
    return matches

def balance_tracker(matches):
    balance = 0

    if matches == 0:
        balance = balance
    elif matches == 1:
        balance = (balance + 4)
    elif matches == 2:
        balance = (balance + 7)
    elif matches == 3:
        balance = (balance + 100)
    elif matches ==4:
        balance = (balance + 50000)
    elif matches == 5:
        balance = (balance + 1000000)
    elif matches == 6:
        balance = (balance + 25000000)
    return balance

def ROI(final_balance, x):
    earnings = (final_balance)
    expenses = (x * -2)
    return_on_investment = (earnings - expenses) / (expenses)
    return return_on_investment

def main():

    final_balance = 0
    x = 0
    winner = pick6()
    while x < 100000:
       
        ticket = pick6()
        match_count = num_matches(winner, ticket)
        final_balance = final_balance + balance_tracker(num_matches(winner, ticket))
        x += 1

    print(f'The winning numbers are: {winner}')
    print(f'Your final balance is: $ {final_balance}')
    print(f'Your return on investment is: {ROI(final_balance, x)}')
    

main()