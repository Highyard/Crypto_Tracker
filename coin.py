
class Coin:

    def __init__(self, name, price, change):
        self.name = name
        self.price = price
        self.change = change

    def __str__(self):
        return "Name: {}, Price: {}, Change: {} ".format(self.name, self.price, self.change)