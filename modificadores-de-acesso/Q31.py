class Arma:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} ataca!")

class Espada(Arma):
    def atacar(self):
        print(f"{self.nome} faz um corte rápido com a lâmina!")

class Arco(Arma):
    def atacar(self):
        print(f"{self.nome} dispara uma flecha à distância!")

arma1 = Espada("Espada Longa")
arma2 = Arco("Arco de Caça")

arma1.atacar()  
arma2.atacar() 
