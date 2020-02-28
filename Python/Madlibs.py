# noun_1 = input('enter a plural noun: ')
# noun_2 = input('enter another noun: ')
# verb_1 = input('enter a verb: ')
# verb_2 = input('enter another verb: ')
# verb_3 = input('enter another verb: ')
# adjective_1 = input('enter an adjective: ')

# print(f'This is my madlib: We\'ve been {verb_1}ing most our {noun_1} living in a {noun_2}\'s paradise. We don\'t {verb_2}, we all {verb_3} {adjective_1}, living in a {noun_2} paradise. ')



# # We've been spending most our lives living in a (noun)
# # paradise. We don't (verb), we all play (adjective), 
# # living in a (noun) paradise.


from random import randint

user_nouns = input('list three nouns separated by commas: ')
noun_list = user_nouns.split(', ')
n = randint(0,2)

user_verbs = input('list three verbs sparated by commas: ')
verb_list = user_verbs.split(', ')
v = randint(0,2)

user_adjectives = input('list three adjectives separated by commas: ')
adjective_list = user_adjectives.split(', ')
a = randint(0, 2)

read_story = 'y'

while read_story == 'y':
    print('Would you like to read the Madlib?')
    read_story = input('Type y for yes or n for no: ')
    if read_story != 'y':   
        break
    print(f'We\'ve been {verb_list[v]}ing most our {noun_list[n]} living in a {noun_list[n]}\'s paradise. We don\'t {verb_list[v]}, we all {verb_list[v]} {adjective_list[a]}, living in a {noun_list[n]} paradise. ')
print('Thanks for playing Madlibs with me!😀')



# x = randint(0,2) # callin the function randint and storing the value it returns in the variable 'x'
# print(x)
# print(user_nouns) # prints list of strings saved in variable 'user_nouns'
# print(user_nouns[x]) # prints the 'x'th element of user_nouns