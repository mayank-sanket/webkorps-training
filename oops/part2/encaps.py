# Encapsulation (hiding the internal implementations)



class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance


acc1 = BadBankAccount(0.0)
# acc1.balance = -90.00 

# print(acc1.balance) # prints -90.0 without any error (not a good thing)


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError ("Withdraw amount must be positive.")

        if amount > self._balance:
            raise ValueError('In sufficient funds!')
        self._balance -= amount


good_acc = BankAccount()
print(good_acc.balance) # 0.0
# good_acc.balance = 12 (cannot do like this, need to have a setter )

good_acc.deposit(200)
print(good_acc.balance)

good_acc.withdraw(100)
print(good_acc.balance)
