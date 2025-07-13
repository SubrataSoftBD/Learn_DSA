class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance # private variable (Encapsulation)
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount("Subrata", 7800)


acc.withdraw(700)

acc.deposit(98000)

acc.deposit(980)
acc.deposit(20)

acc.withdraw(100)


print(f"Mr {acc.name} you have {acc.get_balance()} TK in your account")