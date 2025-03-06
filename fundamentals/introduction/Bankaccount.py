class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.amount +=amount
        return self 
        # your code here
    def withdraw(self, amount):
        # your code here
        if ((self.amount-amount)>0):
            self.amout -=amount
            return self 
        else:

            return (print(f"Insufficient funds: Charging a $5 fee"))

    def display_account_info(self):
        print(self.balance)
        # your code here
  
