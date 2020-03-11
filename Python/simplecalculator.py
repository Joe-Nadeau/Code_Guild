#PDX Code Guild
#Lab 11
#Simple Calculator
#Joey Nadeau


def main():

    def addition(a, b):
        return a + b
    
    def subtraction(a, b):
        return a - b
    
    def multiplication(a, b):
        return a * b
    
    def division(a, b):
        return a / b

    ops = {'+': addition, '-': subtraction, '*': multiplication, '/': division}
    
    print('This is a simple calculator. It will allow you to perform an operation on two variables.\n')
    
    while True:
        a = int(input('Enter number:\n'))
        b = int(input('Enter another number:\n'))

        calculate_math = input('Which operation would you like to perform? \n + = addition \n - = subtraction \n * = multiplication \n / = division \n q = Eff this, get me the math out of here!')

        if calculate_math == '+':
            ops['+']
            print(f'\n{a} + {b} = {addition(a, b)}')
        if calculate_math == '-':
            ops['-']
            print(f'\n{a} - {b} = {subtraction(a, b)}')
        if calculate_math == '*':
            ops['*']
            print(f'\n {a} * {b} = {multiplication(a, b)}')
        if calculate_math == '/':
            ops['/']
            print(f'\n{a} / {b} = {division(a, b)}')   
        elif calculate_math == 'q':
            break

main()
