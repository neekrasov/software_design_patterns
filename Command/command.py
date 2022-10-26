import abc
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}.\n Balance: {self.balance}\n")
    
    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}. \n Balance: {self.balance}\n")
            return True
        return False
    
    def __str__(self):
        return f"Account Balance: {self.balance}\n"

class Command(abc.ABC):

    @abc.abstractmethod
    def invoke(self):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self):
        raise NotImplementedError

class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = "deposit"
        WITHDRAW = "withdraw"

    def __init__(self, account, action, amount):
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)
            
    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)
    
    def __str__(self):
        return f"BankAccountCommand: \n action={self.action},\n amount={self.amount},\n success={self.success}\n"

if __name__ == "__main__":
    ba = BankAccount()
    cmd = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
    cmd.invoke()
    print(cmd)

    cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
    cmd.invoke()
    print(cmd)

    cmd = BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 100)
    cmd.invoke()
    print(cmd)

    print(ba)