class Inimigo:
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca

    def atacar(self):
        print(f"{self.nome} ataca causando {self.forca} de dano!")

class Chefe(Inimigo):
    def atacar(self):
        dano_especial = self.forca * 2
        print(f"{self.nome} usa um golpe especial e causa {dano_especial} de dano!")


inimigo1 = Inimigo("Goblin", 10)
chefe1 = Chefe("Dragão", 20)

inimigo1.atacar()  
chefe1.atacar()    