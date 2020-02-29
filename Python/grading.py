#PDX Code Guild
#Lab 3 - Grading
#Joey Nadeau

print('\nThis program will convert your numerical grade into a letter grade.')

num_grade = input('Enter your numerical grade: ')
num_grade = int(num_grade)
if num_grade > 100:
    print('Way to go Einstein! ')
elif num_grade >= 90 and num_grade <= 100:
    print('Your grade is an A ')
elif num_grade >= 80 and num_grade <= 89:
    print('Your grade is a B ')
elif num_grade >= 70 and num_grade <= 79:
    print('Your grade is a C ')
elif num_grade >= 60 and num_grade <= 69:
    print('Your grade is a D ')
elif num_grade <= 59:
    print('You better try harder bud. ')

