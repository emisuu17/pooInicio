class Inimigo:
    def __init__(self,zumbi):
        self.nome = zumbi
        self.vida = 100

class Personagem:
    def __init__(self,vidap):
        self.vida = vidap
    
    def atacar(self,vidap):
        self.vida -= vidap



Inimigo1 = Inimigo()
Personagem1 = Personagem(100)
print(Inimigo1.atacar())
