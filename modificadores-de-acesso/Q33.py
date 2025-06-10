class Item:
    def __init__(self, nome):
        self.nome = nome

    def usar(self):
        print(f"{self.nome} foi usado.")

class Pocao(Item):
    def usar(self):
        print(f"{self.nome} usada: Você recuperou 50 pontos de vida!")

class Equipamento(Item):
    def usar(self):
        print(f"{self.nome} equipado: Sua força aumentou!")


item1 = Pocao("Poção de Vida")
item2 = Equipamento("Espada de Ferro")

item1.usar()  
item2.usar()  