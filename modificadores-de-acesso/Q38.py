class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def adicionar_pontos(self, valor):
        self.pontos += valor
        print(f"{self.nome} ganhou {valor} pontos. Total: {self.pontos}")

class JogadorPremium(Jogador):
    def adicionar_pontos(self, valor):
        bonus = valor * 2
        self.pontos += bonus
        print(f"{self.nome} é premium e ganhou {bonus} pontos! Total: {self.pontos}")


j1 = Jogador("Lucas")
j2 = JogadorPremium("Ana")

j1.adicionar_pontos(100)  
j2.adicionar_pontos(100)  
