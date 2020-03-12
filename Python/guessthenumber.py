#PDX Code Guild
#Lab 12
#Guess the number
#Joey Nadeau

import random

def main():

    print('Hello human. I am Bemo.') 
    
    while True:
        
        yes_or_no = input('Would you like to play guess the number with me?')

        if yes_or_no == 'no':
            print('OK, goodbye!')
            break
    
        print('OK! I am thinking of a number between 1 and 10. You have 10 chances to guess it correctly')
   
        x = random.randint(1,10)

        a = 0

        while a <= 10:
            a += 1
            user_guess = int(input('What is your guess?'))

            if user_guess == x:
                print(f'Whoa maaaan, are you psychic!? The number I chose was {x}. You got it right!')
                break
            else:
                print('Nope, that\'s not it. Try again')
                if a == 10:
                    print('Wow, you\'re really bad at this! You lose.')

main()
