#PDX Code Guild
#Lab 17
#Palindrome/Anagram Checker
#Joey Nadeau

def check_palindrome(pal_word):
    word_pal = pal_word[::-1]

    for index in range(len(pal_word) // 2):
        if pal_word[index] ==  word_pal[index]:
            continue
        else:
            return False
    return True

def check_anagram(first_word, second_word):
    first_word.lower() # Convert each word to lower case (lower)
    second_word.lower() 
    first_word.replace(" ", "")  # Remove all the spaces from each word (replace)
    second_word.replace(" ", "")      
    # Sort the letters of each word (sorted)
    # Check if the two are equal

def main():

    anag_or_palin = input('Would you like to check for a palindrom or an anagram?: ')

    if anag_or_palin == 'palindrome'.lower():
        pal_word = input('\nEnter a word: \n')
        
        if check_palindrome(pal_word):
            print(f'{pal_word} is a palindrome')
        else:
            print(f'{pal_word} is not a palindrome')

    elif anag_or_palin == 'anagram'.lower():
        first_word = input('\nEnter the first word: \n')
        second_word = input('\nEnter the second word: \n')

main()