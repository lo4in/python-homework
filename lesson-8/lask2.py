import json

class Account:
    def __init__(self, account_number, name, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        return "Insufficient funds or invalid amount."

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
        }

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1).zfill(6)
        if initial_deposit < 0:
            return "Initial deposit must be non-negative."
        new_account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        self.save_to_file()
        return f"Account created successfully. Account Number: {account_number}"

    def view_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return f"Account Number: {account.account_number}, Name: {account.name}, Balance: {account.balance}"
        return "Account not found."

    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.deposit(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            result = account.withdraw(amount)
            self.save_to_file()
            return result
        return "Account not found."

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            json.dump({acc_num: acc.to_dict() for acc_num, acc in self.accounts.items()}, file, indent=4)

    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as file:
                data = json.load(file)
                self.accounts = {acc_num: Account.from_dict(acc) for acc_num, acc in data.items()}
        except FileNotFoundError:
            self.accounts = {}

# Example Usage
if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nWelcome to the Bank Application")
        print("1. Create an Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_deposit = float(input("Enter initial deposit: "))
            print(bank.create_account(name, initial_deposit))

        elif choice == "2":
            account_number = input("Enter account number: ")
            print(bank.view_account(account_number))

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            print(bank.deposit(account_number, amount))

        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            print(bank.withdraw(account_number, amount))

        elif choice == "5":
            print("Thank you for using the Bank Application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
