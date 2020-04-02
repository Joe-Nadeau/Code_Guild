# PDX Code Guild
# Lab 25
# ATM
# Joey Nadeau

class ATM:
    def __init__(self, balance, interest_rate)
        self.balance = balance
        self.interest_rate = interest_rate
    
    # returns the account balance
    def check_balance(self):
        return f'Your current balance is: {self.balance}'

    # Get amount from user, add it to balance
    def deposit(amount):
        balance = balance + amount
        return f'You have deposited ${amount} into your account.\n Your new balance is ${balance}.'

    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(amount):
        if (balance - amount) >= 0:
            return True
        else:
            return f'The amount you have entered exceeds your current balance.\nYour current balance is: ${balance}. \nPlease enter a different amount: '

    # withdraws the amount from the account and returns it
    def withdraw(amount):
        if check_withdrawal == True:
            balance = balance - amount
            return f'Here is the amount you have withdrawn ${amount}.\n Your remaining balance is ${balance}.'

    #returns the amount of interest calculated on the account
    def calc_interest(self):
        return f'Your interest rate is: {self.interest_rate}'

def choose_transaction():

    trans_type = input('Which type of transaction would you like to perform?\nCheck_Balance\nDeposit\nWithdraw\nCalculate_Interest')
