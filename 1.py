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

# Пример использования класса
account1 = BankAccount("Иванов", "1234567890", 1000)
print(account1)

account1.deposit(500)
account1.withdraw(200)

print(account1)
