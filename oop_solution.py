class ShoppingCart:
  def __init__(self):
    self.total = 0
    self.items = {}

  def add_item(self, item_name, quantity, price):
    self.total += quantity * price
    self.items[item_name] = quantity

  def remove_item(self, item_name, quantity, price):
    if item_name not in self.items:
      return
    if quantity >= self.items[item_name]:
      self.total -= self.items[item_name] * price
      del self.items[item_name]
    else:
      self.total -= quantity * price
      self.items[item_name] = self.items[item_name] - quantity

  def checkout(self, cash_paid):
    if cash_paid < self.total:
      return "Cash paid not enough"
    else:
      return cash_paid - self.total


class Shop(ShoppingCart):
  def __init__(self):
    self.quantity = 100

  def remove_item(self):
    self.quantity -= 1
