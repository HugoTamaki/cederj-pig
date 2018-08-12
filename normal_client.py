from client import *

class NormalClient(Client):
  def transfer(self, client, value):
    if self.bank != client.bank:
      if self.balance > value + 10:
        self.balance = self.balance - (value + 10)
        client.deposit(value)
    else:
      super().transfer(client, value)
