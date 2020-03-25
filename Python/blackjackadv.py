#PDX Code Guild
#Lab 19
#Black Jack Advice
#Joey Nadeau


def hand_total_func(user_hand_list, card_values):
    
    sum = 0
    
    for i in user_hand_list:
        # print(i)
        for key, value in card_values.items():
            # print(key, value)
            if key == i:
                # return(value)
                sum = value + sum
    return sum

def Aces(hand_total):

    if hand_total + 11 > 21:
        return 1
    else:
        return 11

def main():

    print('I will give you black jack advice based on the cards you have in your hand.')

    user_hand = (input('Enter 3 cards separated by commas.\n A = Ace\n K = King\n Q = Queen\n J = Jack\n For the number cards just type the number:\n'))
    user_hand_list = user_hand.split(',')
    
    print(user_hand_list)

    card_values = {
                    'A': 0,
                    'K': 10,
                    'Q': 10,
                    'J': 10,
                    '10': 10,
                    '9': 9,
                    '8': 8,
                    '7': 7,
                    '6': 6,
                    '5': 5,
                    '4': 4,
                    '3': 3,
                    '2': 2
                    }

    hand_total = hand_total_func(user_hand_list, card_values)


    if 'A' in user_hand_list:
        Ace_value = Aces(hand_total)
        print(hand_total + Ace_value)
        if hand_total + Ace_value < 17:
            print("I advise that you: hit")
        elif hand_total + Ace_value >= 17 and hand_total + Ace_value < 21:
            print("I advise that you: stay")
        elif hand_total + Ace_value == 21:
            print("I advise that you: yell BLACKJACK!!!")
        elif hand_total + Ace_value > 21:
            print("You are BUSTED and I advise that you: quit before you get in too deep.")
    elif hand_total < 17:
        print("I advise that you: hit")
    elif hand_total >= 17 and hand_total < 21:
        print("I advise that you: stay")
    elif hand_total == 21:
        print("I advise that you: yell BLACKJACK!!!")
    elif hand_total > 21:
        print("You are BUSTED and I advise that you: quit before you get in too deep.")

main()