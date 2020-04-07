class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.n_coins = 0

    def can_add(self, v):
        return self.n_coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.n_coins += v
