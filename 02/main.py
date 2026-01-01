from utils.bank_account import BankAccount

if __name__== "__main__":
    bank_account1 = BankAccount("Alice")
    bank_account1.deposit(1000)
    print(bank_account1.get_balance())

    bank_account1.withdraw(900)
    print(bank_account1.get_balance())
    bank_account1.set_interest_rate(0.1)
    bank_account1.apply_interest()
    print(bank_account1.get_balance())

