class Voador:
    def voar(self):
        print("Estou voando!")


class Inimigo:
    def atacar(self):
        print("Atacando!")

class Dragao(Inimigo, Voador):
    def __init__(self, nome):
        self.nome = nome

dragao = Dragao("Fogo de Dragão")
dragao.voar() 
dragao.atacar()
