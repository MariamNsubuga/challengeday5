class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def open(self):  #returns a bool whether the object is open or not
        self.is_open = True

    def get_balance(self):
        if not self.is_open:
            raise ValueError('No account number matching!')

        return self.balance

    def deposit(self, amount):
        if not self.is_open:
            raise ValueError('No account number matching!')

        if amount <= -1:
            raise ValueError('input correct amount')

        self.balance += amount

    def withdraw(self, amount):
        if not self.is_open:
            raise ValueError('No account number matching!')
            
        if amount > self.balance:
            raise ValueError(' Insufficient funds')

        if amount <= -1:
            raise ValueError(' Put valid amount')

        self.balance -= amount

    def close(self):
        self.is_open = False