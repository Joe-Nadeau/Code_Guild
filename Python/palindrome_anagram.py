#PDX Code Guild
#Lab 17
#Palindrome/Anagram Checker
#Joey Nadeau

def check_palindrome(pal_word):
    word_pal = backward_string(pal_word)

    for char in range(len(pal_word)):
        if char in pal_word == char in word_pal:
            print ('true')
        else:
            print('false')

def backward_string(pal_word):
    strbuild = ""
    for i in pal_word:
        strbuild = i + strbuild
        return strbuild

def main():
    pal_word = input('\nEnter a word: \n')
    check_palindrome(pal_word)

main()