# static methods: belong to the class itself and not the instances
# for this, @staticmethod decorator is used

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"{self.owner}'s account balance {self._balance} Rupees")
        else:
            print('Deposit amount must be positive.')
    
    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <= 5
    


account1  = BankAccount('Mayank', 500000)
account1.deposit(40000)

print(BankAccount.is_valid_interest_rate(12)) # False   | accessing it directly from the class 
print(BankAccount.is_valid_interest_rate(2)) # True