# Определение класса BankAccount
class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Счет пополнен на {amount} тг. Новый баланс: {self.balance} тг.")
        else:
            print("Неверная сумма для пополнения.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Сумма {amount} тг. снята со счета. Новый баланс: {self.balance} тг.")
        else:
            print("Недостаточно средств на счете или неверная сумма для снятия.")

    def __str__(self):
        return f"Владелец счета: {self.owner_name}\nНомер счета: {self.account_number}\nБаланс: {self.balance} тг."

# Определение класса SavingAccount
class SavingAccount(BankAccount):
    def __init__(self, owner_name, account_number, balance=0, interest_rate=0):
        super().__init__(owner_name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Начислены проценты в размере {interest} тг. Новый баланс: {self.balance} тг.")

# Пример использования класса
savings_account = SavingAccount("Петров", "0987654321", 1000, 5)
print(savings_account)

savings_account.deposit(500)
savings_account.add_interest()

print(savings_account)

