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

user_verbs = input('list three verbs sparated by commas: ')
verb_list = user_verbs.split(', ')

user_adjectives = input('list three adjectives separated by commas: ')
adjective_list = user_adjectives.split(', ')

print(f'We\'ve been {verb_list}ing most our {noun_1} living in a {noun_2}\'s paradise. We don\'t {verb_2}, we all {verb_3} {adjective_1}, living in a {noun_2} paradise. ')
