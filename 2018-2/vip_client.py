from client import *

class VipClient(Client):
  def __init__(self, name, balance, bank, registration_number):
    super().__init__(name, balance, bank)
    self.registration_number = registration_number

  def describe(self):
    super().describe()
    print("Numero de registro: " + self.registration_number)
