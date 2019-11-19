from datetime import date


class Transaction:
    def __init__(self, amount, category, initial_amount):
        self.amount = amount
        self.category = category
        self.initial_amount = initial_amount
        self.date = date.today()

    @property
    def description(self):
        return f'Transaction date: {self.date} \nTransaction category: {self.category}'


class Deposit(Transaction):
    def __init__(self, amount, category, tax_rate, initial_amount):
        Transaction.__init__(self, amount, category, initial_amount)
        self.tax_rate = tax_rate

    def calculate_tax(self):
        return self.tax_rate * self.amount * 0.01

    def process(self):
        return self.initial_amount + self.amount - self.calculate_tax()


class Withdrawal(Transaction):
    def __init__(self, amount, category, tax_rate, initial_amount):
        Transaction.__init__(self, amount, category, initial_amount)
        self.tax_rate = tax_rate

    def calculate_tax(self):
        return self.tax_rate * self.amount * 0.1

    def process(self):
        balance = self.initial_amount - self.amount - self.calculate_tax()
        if balance < 0:
            print('There is not enough money on your account')
            return self.initial_amount
        return balance


transaction = Transaction(20, 'salary', 100)
print(transaction.date)
print(transaction.category)
print(transaction.initial_amount)
print(transaction.description)

deposit = Deposit(33, 'bonus', 15, 100)
print(deposit.date)
print(deposit.category)
print(deposit.description)
print(deposit.process())

withdrawal = Withdrawal(33, 'fee', 5, 100)
print(withdrawal.date)
print(withdrawal.category)
print(withdrawal.description)
print(withdrawal.process())

withdrawal = Withdrawal(1000, 'city_tax', 5, 100)
print(withdrawal.date)
print(withdrawal.category)
print(withdrawal.description)
print(withdrawal.process())

