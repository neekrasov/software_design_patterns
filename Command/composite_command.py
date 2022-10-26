import abc
from enum import Enum
import unittest


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
    def __init__(self) -> None:
        self.success = False

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
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

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

class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=None):
        super().__init__()
        if items is not None:
            self.extend(items)
    
    def invoke(self):
        for cmd in self:
            cmd.invoke()
    
    def undo(self):
        for cmd in reversed(self):
            cmd.undo()
    
    def __str__(self):
        return f"CompositeBankAccountCommand: \n {super().__str__()}\n"

class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountCommand(from_acct, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount)
        ])
    
    def invoke(self):
        status = True
        for cmd in self:
            if status:
                cmd.invoke()
                status = cmd.success
            else:
                cmd.success = False
        self.success = status
    
    def __str__(self):
        return f"MoneyTransferCommand: \n {super().__str__()}\n"

class TestSiute(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        cmd = CompositeBankAccountCommand([
            BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100),
            BankAccountCommand(ba, BankAccountCommand.Action.WITHDRAW, 1000)
        ])
        cmd.invoke()
        cmd.undo()

    def test_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        tranfser = MoneyTransferCommand(ba1, ba2, 100)
        tranfser.invoke()
        print("ba1: ", ba1)
        print("ba2: ", ba2)
        tranfser.undo()
        print("ba1: ", ba1)
        print("ba2: ", ba2)

if __name__ == "__main__":
    unittest.main()