
class Pessoa():
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def say_hello(self):
    print("Olar, eu sou o " + self.nome)
    print("eu tenho " + str(self.idade) + " anos")
