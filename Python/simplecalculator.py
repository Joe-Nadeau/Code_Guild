#PDX Code Guild
#Lab 11
#Simple Calculator
#Joey Nadeau


# def main():

#     def addition(a, b):
#         return a + b
    
#     def subtraction(a, b):
#         return a - b
    
#     def multiplication(a, b):
#         return a * b
    
#     def division(a, b):
#         return a / b

#     ops = {'+': addition, '-': subtraction, '*': multiplication, '/': division}
    
#     print('This is a simple calculator. It will allow you to perform an operation on two variables.\n')
    
#     while True:
#         a = int(input('Enter number:\n'))
#         b = int(input('Enter another number:\n'))

#         calculate_math = input('Which operation would you like to perform? \n + = addition \n - = subtraction \n * = multiplication \n / = division \n q = Eff this, get me the math out of here!')

#         if calculate_math == '+':
#             ops['+']
#             print(f'\n{a} + {b} = {addition(a, b)}')
#         if calculate_math == '-':
#             ops['-']
#             print(f'\n{a} - {b} = {subtraction(a, b)}')
#         if calculate_math == '*':
#             ops['*']
#             print(f'\n {a} * {b} = {multiplication(a, b)}')
#         if calculate_math == '/':
#             ops['/']
#             print(f'\n{a} / {b} = {division(a, b)}')   
#         elif calculate_math == 'q':
#             break

# main()

#*************************************************************************
# Version 3

def main():

    print('Hello human, I am but a humble function here to help you with math problems.\nMy name is \'Eval\'.')

    while True:
        
        math_problem = input('Please enter a simple arithmetic problem and I will solve it for you:')

        if math_problem != 'no' or 'quit' or 'exit':
            
            eval(math_problem)
            print(f'{math_problem} = {eval(math_problem)}')
            
        continue_or_quit = input('Would you like me to solve another problem for you? <y/n>')

        if continue_or_quit == 'n':
            break

main()