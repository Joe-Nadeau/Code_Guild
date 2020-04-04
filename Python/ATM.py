# PDX Code Guild
# Lab 25
# ATM
# Joey Nadeau

# ---------CLASSES-----------

class ATM:
    def __init__(self, account_holder = 'John Doe', balance = 0, interest_rate = 0.1, transactions = []):
        self.account_holder = account_holder
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions
    
    # returns the account balance
    def check_balance(self):
        return f'Your current balance is: ${self.balance}\n'

    # Get amount from user, add it to balance
    def deposit(self, amount):
        self.balance = self.balance + amount
        return f'You have deposited ${amount} into your account.\n Your new balance is ${self.balance}.'

    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True
        else:
            return f'The amount you have entered exceeds your current balance.\nYour current balance is: ${self.balance}. \nPlease enter a different amount: '

    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance = self.balance - amount
            return f'Here is the amount you have withdrawn ${amount}.\n Your remaining balance is ${self.balance}.'

    # stores the transactions made by the user
    def print_transactions(self):
        return self.transactions
    #returns the amount of interest calculated on the account
    # def calc_interest(self, amount):
    #     return f'Your interest rate is: {self.interest_rate}'


#  ------- FUNCTIONS ---------

# def create_new_account():
#     new_guy = input('Please enter the first and last name of the new account holder: \n')
#     locals()[new_guy] = ATM('', 12, ('the land of oo', 'somewhere else', 'who knows'))

def choose_transaction(bobby):

    while True:
        trans_type = input('Which type of transaction would you like to perform?\nCheck_Balance\nDeposit\nWithdraw\nCalculate_Interest\nPrint Transactions\nExit-ATM')

        if trans_type == 'Check_Balance':
            print(bobby.check_balance())
            (bobby.transactions()).append('Check balance')
        elif trans_type == 'Deposit':
            amount = float(input('Please enter the amount you would like to deposit:\n'))
            print(bobby.deposit(amount))
            (bobby.transactions()).append(f'Deposit of ${amount}')
        elif trans_type == 'Withdraw':
            amount = float(input('Please enter the amount you would like to withdraw:\n'))
            print(bobby.withdraw(amount))
            (bobby.transactions()).append(f'Withdraw of ${amount}')
        elif trans_type == 'Calculate Interest':
            print(bobby.calc_interest(amount))
        elif trans_type == 'Print Transactions':
            bobby.print_transactions()
        elif trans_type == 'Exit-ATM':
            print('Goodbye')
            break



# --------- Main ----------

def main():

    # instantiates class 'ATM'
    bobby = ATM('Bobby', 2000, 0.1, [])

    # call functions
    choose_transaction(bobby)

main()
