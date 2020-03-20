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

def main():
    pal_word = input('\nEnter a word: \n')
    
    if check_palindrome(pal_word):
        print(f'{pal_word} is a palindrome')
    else:
        print(f'{pal_word} is not a palindrome')

main()