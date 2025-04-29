import random

class Personagem:
    def __init__(self,nome):
        self.nome = nome
        self.vida = 100
        self.atk = 10


class Inimigo:
    def __init__(self,nome):
        self.nome = nome
        self.vida = 100


    def atacar(self):
        return random.randint(5,20)
        
       