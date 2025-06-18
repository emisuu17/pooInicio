class AnimalMontaria:
    def montar(self):
        print("Montado na criatura!")

class Guerreiro:
    def atacar(self):
        print("Atacando inimigo!")


class Cavaleiro(Guerreiro, AnimalMontaria):
    def __init__(self, nome):
        self.nome = nome

cavaleiro = Cavaleiro("Griffith")
cavaleiro.atacar()  
cavaleiro.montar()
