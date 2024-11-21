if __name__ == "__main__":
    from bank_accounts import *

    Penguin = BankAccount(1000000, "Penguin")
    Giraffe = BankAccount(200000, "Giraffe")
    Kora = BankAccount(2000000, "Kora")
    Panda = BankAccount(30000, "Panda")

    Penguin.transfer(10000000, Panda)




