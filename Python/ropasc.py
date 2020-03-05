# PDX Code Guild
# Lab 7
# Rock Paper Scissors

import random

def winner():

    weapon = ['rock', 'paper', 'scissors']
    cpu_weapon = random.choice(weapon)
    user_weapon = input('Choose your weapon: \nrock, \npaper, \nor \nscissors \n')

    if cpu_weapon == 'rock' and user_weapon == 'rock':
        print('It\'s a tie!')
    elif cpu_weapon == 'rock' and user_weapon == 'paper':
        print('You win, I lose!')
    elif cpu_weapon == 'rock' and user_weapon == 'scissors':
        print('I win, you lose!')
    elif cpu_weapon == 'paper' and user_weapon == 'paper':
        print('It\'s a tie!')
    elif cpu_weapon == 'paper' and user_weapon == 'scissors':
        print('You win, I lose!')
    elif cpu_weapon == 'paper' and user_weapon == 'rock':
        print('I win, you lose!')
    elif cpu_weapon == 'scissors' and user_weapon == 'scissors':
        print('It\'s a tie!')
    elif cpu_weapon == 'scissors' and user_weapon == 'rock':
        print('You win, I lose!')
    elif cpu_weapon == 'scissors' and user_weapon == 'paper':
        print('I win, you lose!')
    
def main():

    while True:
        winner()
        play_again = input('Would you like to play again?: <y/n>')
        if play_again == 'n':
            print('Fine! I thought humans were supposed to be fun. Are you sure you\'re not a computer?')
            break        
main()
        