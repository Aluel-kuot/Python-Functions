
class BankAccount:
    type="Serving Acaount"
    def __init__(self,account_number,balance,account_name,interest_rate):
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
        self.interest_rate=interest_rate
        
    def  deposit_money(self,amount):
        self.balance+=amount
        return f"{self.account_name} has {self.balance} in the {self.account_number}"
 

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
        else:
            return "Insufficient funds."

    def calculate_interest(self, time):
        interest = (self.balance * self.interest_rate * time) / 100
        return f"Interest for {time} years: {interest}"


