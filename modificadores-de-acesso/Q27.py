class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

    def status(self):
        print(f"{self.nome} - Vida: {self.vida}, Força: {self.forca}")

class Chefe(Inimigo):
    def __init__(self, nome):
        vida = 200
        forca = 60
        super().__init__(nome, vida, forca)

chefe1 = Chefe("Dragão Final")
chefe1.status()

