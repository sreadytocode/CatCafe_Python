class Cafe:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drink_stock = {}

    def drink_stock_level(self, drink):
        if drink in self.drink_stock:
            return self.drink_stock[drink]
        else:
            return 0

    def drink_stock_value(self):
        total = 0

        for drink in self.drink_stock:
            total += (drink.price * self.drink_stock[drink])

        return total

    def add_drink(self, drink):
        if drink in self.drink_stock:
            self.drink_stock[drink] += 1
        else:
            self.drink_stock[drink] = 1