# protected and private methods



class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance
    
    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            # print(f"{self.owner}'s account balance {self._balance} Rupees")
            self.__log_transaction('deposit', amount)
        else:
            print('Deposit amount must be positive.')
    
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of Rupees {amount}. New Balance: {self._balance} Rupees")

    def _is_valid_amount(self, amount):
        return amount > 0

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0<= rate <= 5
    
    



account1  = BankAccount('Mayank', 500000)
account1.deposit(40000)

print(BankAccount.is_valid_interest_rate(12)) # False   | accessing it directly from the class 
print(BankAccount.is_valid_interest_rate(2)) # True


# account1.__log_transaction('deposit', 54544) # error (because that is a private method)