class Bank:

    def __init__(self, balance: List[int]):
        self.bal = balance
        self.n = len(balance)

    def valid(self, acc):
        return 1 <= acc <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.valid(account1) and self.valid(account2) and money <= self.bal[account1 - 1]:
            self.bal[account1 - 1] -= money
            self.bal[account2 - 1] += money
            return True
        return False


    def deposit(self, account: int, money: int) -> bool:
        if self.valid(account):
            self.bal[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.valid(account) and self.bal[account - 1] >= money:
            self.bal[account - 1] -= money
            return True
        return False