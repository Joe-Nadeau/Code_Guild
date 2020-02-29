#PDX Code Guild
#Lab 3 - Grading
#Joey Nadeau

print('\nThis program will convert your numerical grade into a letter grade.')

def grade_converter(num_grade):
    if num_grade % 10 > 5: 
        qualifier = '+'
    elif num_grade % 10 == 5:
        qualifier = ''
    elif num_grade % 10 < 5:
        qualifier = '-'
    return qualifier

while True:

    num_grade = input('Enter your numerical grade: ')
    num_grade = float(num_grade)
    if num_grade > 110:
        print('Way to go Einstein! ')
    elif num_grade >= 100.01 and num_grade <= 110:
        print('Wow, you got an A+! You must be really smart or...what\'s that on your nose?')
    elif num_grade >= 90 and num_grade <= 100:
        qualifier = grade_converter(num_grade)
        print('Your grade is an: A' + qualifier)
    elif num_grade >= 80 and num_grade <= 89.9:
        qualifier = grade_converter(num_grade)
        print('Your grade is a B ' + qualifier)
    elif num_grade >= 70 and num_grade <= 79.9:
        qualifier = grade_converter(num_grade)
        print('Your grade is a C ' + qualifier)
    elif num_grade >= 60 and num_grade <= 69.9:
        qualifier = grade_converter(num_grade)
        print('Your grade is a D ' + qualifier)
    elif num_grade < 60:
        print('You better try harder bud. ')

    if input('Would you like to convert another grade?:(y/n)').lower() == 'n':
        break