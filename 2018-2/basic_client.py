from client import *

class BasicClient(Client):
  def transfer(self, client, value):
    if self.balance > value + 10:
      self.balance = self.balance - (value + 10)
      client.deposit(value)
