
class BankAccount:
    type="Serving Acaount"
    def __init__(self,account_number,balance,account_name,interest_rate,loan_balance,
    deposit,withdrawals):
        # quiz1
        self.account_number=account_number
        self.account_name=account_name
        self.balance=balance
        self.interest_rate=interest_rate
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

        
    def  deposit_money(self,amount):
        self.balance+=amount
        transaction = {"amount": amount, "narration": "deposit"}
        self.deposits.append(transaction)
        return f"{self.account_name} has {self.balance} in the {self.account_number}"
 
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = {"amount": amount, "narration": "withdrawal"}
            self.withdrawals.append(transaction)
            return f"Withdrawal successful. New balance: {self.balance}"
        else:
            return "Insufficient funds."

    def calculate_interest(self, time):
        interest = (self.balance * self.interest_rate * time) / 100
        return f"Interest for {time} years: {interest}"

# quiz2
    def check_balance(self):
        return  f"Your current balance is{self.balance}"

        # //quiz3
    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({
            "amount": amount,
            "narration": "deposit"
        })

        # //quiz4
    def withdrawal(self, amount):
        if self.balance < amount:
          return("Insufficient balance")
        self.balance -= amount
        self.withdrawals.append({
            "amount": amount,
            "narration": "withdrawal"
        })

        # //quiz5
    def print_statement(self):
        for transaction in self.deposits + self.withdrawals:
            print(f"{transaction['narration']} - {transaction['amount']}")

            # //quiz6

    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return("Account has outstanding loan")
        if amount < 100:
            return f"Loan amount must be more than 100"

        if len(self.deposits) <= 10:
            return f"Customer must make at least 10 deposits"
        if amount > sum(d["amount"] for d in self.deposits) / 3:
            return f"Loan amount must be less than or equal to 1/3 of total deposits"
        self.loan_balance += amount
    def repay_loan(self, amount):
        if self.loan_balance < amount:
            return f"Loan amount is more than outstanding loan"
        self.loan_balance -= amount
        self.balance += amount
    def transfer(self, amount, account):
        if amount > self.balance:
            return f"Insufficient funds. Your current balance is {self.balance}"
        else:
            self.balance -= amount
            account.deposit(amount)
            return f"You have successfully transferred {amount} to account {account.account_number}. Your new balance is ${self.balance}"



   