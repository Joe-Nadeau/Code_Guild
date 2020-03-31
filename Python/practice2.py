# PDX Code Guild
# Practice 2: Strings
# Joey Nadeau

# Problem 1

def double_every_other():

    user_string_in= input("Enter some text here: ")
    user_string_in = user_string_in.replace(" ", "")
    user_string_out = []

    for i in range(len(user_string_in)):
        if (i%2) == 0:
            user_string_out.append(user_string_in[i]*2)
        else:
            user_string_out.append(user_string_in[i])
    user_string_out = ''.join(user_string_out)
    return user_string_out

#print(double_every_other())

# Problem 2

def missing_char():
    a = "globerfish"
    incomplete_string = []

    for char in a:
        
        b = a.replace(char, "")
        incomplete_string.append(b)
    return incomplete_string

#print(missing_char())

# Problem 3

def latest_letter():

    word = input("Enter a word: ")
    x = sorted(word)
    y = x.pop()
    return f'The latest leter is: {y}'

# print(latest_letter())

# Problem 4

def count_hi():

    a_string = 'hi my name is bob. hi bob, my name is tom, hi tom, my name is carl, hi carl, my name is hihihi.'
    hi_count = a_string.count('hi')
    return hi_count

#print(f'The hi count is: {count_hi()}')




