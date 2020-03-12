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
        guess_count = 0
        last_guess = 0

        while True:

            current_guess = int(input('What is your guess?'))
            guess_count += 1
            previous_diff = abs(x - last_guess) 
            current_diff = abs(x - current_guess)

            if current_guess == x:
                print(f'Whoa maaaan, are you psychic!? The number I chose was {x}. You got it right!')
                print(f'It took you {guess_count} guesses to get it right.')
                break
            elif current_guess > x:
                print('Your guess is too high. Try again.')
            elif current_guess < x:
                print('Your guess is too low. Try again.')
            
            if guess_count > 1:
                if previous_diff > current_diff:
                    print("You\'re getting warmer.")
                elif previous_diff < current_diff:
                    print("You\'re getting colder.")
                else:
                    print('You guessed the same number goober. Try again.')
            
            last_guess = current_guess
            

main()
