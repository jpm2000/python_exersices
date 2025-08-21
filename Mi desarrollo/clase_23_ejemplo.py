# Names example

class Person:
    # This is the constructor of the class Person
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hi my name is {self.name} and I'm {self.age} years old")

# Objects:

person1 = Person("Juan Pablo", 24)
person2 = Person("Sylvana", 25)

person1.greet()
person2.greet()

print('--------------------------------')

# Banking exmaple

class BankAccount:
    def __init__(self, name, balance, credit_card, bank_name):
        self.name = name
        self.balance = balance
        self.credit_card = credit_card
        self.bank_name = bank_name
        # when I need to use a boolean value, True or False, I don't need to add the value in the constructor
        self.account_active = True
        self.credit_card_active = True


    def deposit(self, deposit_amount, date, time):
        if self.account_active:
            self.balance += deposit_amount
            self.date = date
            self.time = time
            # Show the deposit information and the balance
            print(f'Hi {self.name} you have deposited {deposit_amount} on {self.date} at {self.time}. Your current balance is growing, now you have {self.balance}!!!')
        else: 
            print(f"Hi {self.name} you account is sleeping, please wake it up")
    
    def withdraw(self, withdraw_amount, date, time):
        if self.account_active:
            if self.balance >= withdraw_amount:
                self.balance -= withdraw_amount
                self.date = date
                self.time = time
            # Show the new balance
                print(f'Hi {self.name} you have withdrawn {withdraw_amount} on {self.date} at {self.time}. I hope it is an investment, because your current balance is {self.balance}')
        else:
            print(f"I'm sorry, you are out of funds, get back to work")
                    
    def deactivate(self):
        self.account_active = False
        print("The account is sleeping")

    def active(self):
        self.account_active = True
        print("The account is ready to work again!")

account1 = BankAccount("Juan Pablo", 5000, "yes", "Nu")
account2 = BankAccount("JP", 15000, "no", "Davivienda")

# Deposit

account1.deposit(500, "24/10/2000", "18:00 pm")
account2.deposit(100, "25/10/2000", "18:01")
account2.deactivate()
account2.deposit(100, "25/10/2000", "18:01")
account2.active()
account2.deposit(200, "26/10/2000", "18:01")
account1.withdraw(50, "22/11/2000", "18:02")


