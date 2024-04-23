class BankAccount:
    def __init__(self, owner_name, account_number, balance=0):
        self._owner_name = owner_name
        self._account_number = account_number
        self._balance = balance

    def get_owner_name(self):
        return self._owner_name

    def set_owner_name(self, owner_name):
        self._owner_name = owner_name

    def get_account_number(self):
        return self._account_number

    def set_account_number(self, account_number):
        self._account_number = account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("Баланс не может быть отрицательным.")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Счет пополнен на {amount} тг. Новый баланс: {self._balance} тг.")
        else:
            print("Неверная сумма для пополнения.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Сумма {amount} тг. снята со счета. Новый баланс: {self._balance} тг.")
        else:
            print("Недостаточно средств на счете или неверная сумма для снятия.")

    def __str__(self):
        return f"Владелец счета: {self._owner_name}\nНомер счета: {self._account_number}\nБаланс: {self._balance} тг."

    def __eq__(self, other):
        return self._balance == other.get_balance()

    def __lt__(self, other):
        return self._balance < other.get_balance()

    def __gt__(self, other):
        return self._balance > other.get_balance()

# Пример использования класса
account1 = BankAccount("Иванов", "1234567890", 1000)
account2 = BankAccount("Петров", "0987654321", 2000)

print("Сравнение счетов по балансу:")
print("account1 == account2:", account1 == account2)
print("account1 < account2:", account1 < account2)
print("account1 > account2:", account1 > account2)
