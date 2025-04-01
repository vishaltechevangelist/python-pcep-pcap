class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self):
        pass

    def withdraw(self, account_to_debit, amount_to_debit):
        if not int(self.balance) < amount_to_debit:
            self.balance -= amount_to_debit
        else:
            print("Insufficient amount, can't be debit the {} account".format(account_to_debit))


    def getBankAccountDetail(self):
        return {self.account_number:{'name':self.account_holder, 'balance':self.balance}}


class Bank:
    list_of_bank_account = []

    def add_account(self, bank_account):
        Bank.list_of_bank_account.append(bank_account)

    def remove_account(self, acc_to_delete):
        for index, bank_account_item in enumerate(Bank.list_of_bank_account):
            if bank_account_item.__dict__["account_number"] == acc_to_delete:
                Bank.list_of_bank_account.pop(index)

    def get_total_assets(self):
        total_assets = 0
        for bank_account_item in Bank.list_of_bank_account:
            total_assets += int(bank_account_item.__dict__["balance"])
        return total_assets

bank_account1 = BankAccount(1, "Vishal", "20000000")
bank_account2 = BankAccount(2, "Priyanka", "2000000")
bank_account3 = BankAccount(3, "Dinesh", "10000000")


bank = Bank()
bank.add_account(bank_account1)
bank.add_account(bank_account2)
bank.add_account(bank_account3)

# print(bank.get_total_assets())
bank.remove_account(2)
print(bank.get_total_assets())

bank_account1.withdraw(1, 30000000)

