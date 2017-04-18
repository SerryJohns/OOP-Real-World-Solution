class ShoppingCart:
    def __init__(self):
        self.__total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.__total += quantity * price
        self.items[item_name] = quantity

    def remove_item(self, item_name, quantity, price):
        if item_name not in self.items:
            return
        if quantity >= self.items[item_name]:
            self.__total -= self.items[item_name] * price
            del self.items[item_name]
        else:
            self.__total -= quantity * price
            self.items[item_name] = self.items[item_name] - quantity

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return "Cash paid not enough"
        else:
            return cash_paid - self.total


class Shop(ShoppingCart):
    def __init__(self):
        pass
    
    def sale(self, item_name, qty, price):
        ShoppingCart.add_item(item_name, qty, price)

