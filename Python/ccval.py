#PDX Code Guild
#Lab 20
#Credit Card Validation
#Joey Nadeau


def main():

CC_number = input("Enter the 16 digit credit card number that you would like to validate: \n")
CC_numstring = list(map(int, CC_number))
print(CC_numstring)
CC_numstring = CC_numstring[:-1]
print(CC_numstring)
CC_numstring = CC_numstring[::-1]
print(CC_numstring)

for i in range(1, len(CC_numstring), 2):
    CC_numstring[i] *= 2
print(f'{CC_numstring}\n')

for i in CC_numstring:
    if i > 9:
        x = CC_numstring.index(i)
        CC_numstring[x] = i - 9
print(CC_numstring)

main()

