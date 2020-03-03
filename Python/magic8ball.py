# PDX Code Guild
# Lab 4
# magic8ball

import random

eightball_answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Seriously wtf bud, ask me a different question', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('Hello looser...uh, um...I mean user...haha jk. I am the great and powerful Magic 8 Ball! Stare in awe at my greatness!...Just kidding, I\'m not that full of myself. Ok, let\'s get to business. So, basically I can answer yes/no questions.')

def QNA():
    user_question = input('Type your question: ')
    print(user_question)
    print(random.choice(eightball_answers))

QNA()

while True:

    anotherQ = input('Would you like to ask me another question? y/n ').lower()
    if anotherQ == 'y': 
        QNA()
    elif anotherQ == 'n':
        break
    else:
        print('Please type y or n')

