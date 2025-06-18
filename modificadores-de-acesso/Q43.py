class Curador:
    def curar(self):
        print("Curando aliado!")

class Guerreiro:
    def atacar(self):
        print("Atacando inimigo!")

class Paladino(Guerreiro, Curador):
    def __init__(self, nome):
        self.nome = nome


paladino = Paladino("guts")
paladino.atacar() 
paladino.curar() 
