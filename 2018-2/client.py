class Client():
  def __init__(self, name, balance, bank):
    self.name = name
    self.balance = balance
    self.bank = bank

  def describe(self):
    print("Meu nome eh " + self.name)
    print("Meu saldo eh " + str(self.balance))
    print("Meu banco eh " + self.bank)

  def deposit(self, value):
    self.balance = self.balance + value

  def pay(self, value):
    if self.balance > value:
      self.balance = self.balance - value

  def transfer(self, client, value):
    if self.balance > value:
      self.balance = self.balance - value
      client.deposit(value)
