# PDX Code Guild
# Lab 25
# ATM
# Joey Nadeau

# ---------CLASSES-----------

class ATM:
    def __init__(self, account_holder, balance, interest_rate):
        self.account_holder = account_holder
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
        if check_withdrawal(amount) == True:
            balance = balance - amount
            return f'Here is the amount you have withdrawn ${amount}.\n Your remaining balance is ${balance}.'

    #returns the amount of interest calculated on the account
    def calc_interest(amount):
        return f'Your interest rate is: {self.interest_rate}'


#  ------- FUNCTIONS ---------

# def create_new_account():
#     new_guy = input('Please enter the first and last name of the new account holder: \n')
#     locals()[new_guy] = ATM('', 12, ('the land of oo', 'somewhere else', 'who knows'))

def choose_transaction():

    trans_type = input('Which type of transaction would you like to perform?\nCheck_Balance\nDeposit\nWithdraw\nCalculate_Interest\nExit-ATM')

    if trans_type == 'Check_Balance':
        print(account_holder.check_balance(self))
    elif trans_type == 'Deposit':
        amount = float(input('Please enter the amount you would like to deposit:\n'))
        print(account_holder.deposit(amount))
    elif trans_type == 'Withdraw':
        amount = float(input('Please enter the amount you would like to withdraw:\n'))
        print(account_holder.withdraw(amount))
    elif trans_type == 'Calculate_Interest':
        print(account_holder.calc_interest(amount))
    elif trans_type == 'Exit-ATM':
        break



# --------- Main ----------

def main():

    # instantiates class 'ATM'
    my_account = ATM('Bobby', 0, 0.1)

    # define variables
    amount = 0

    # call functions
    choose_transaction()

main()
