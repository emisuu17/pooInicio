class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def vencer_desafio(self):
        self.pontos += 10
        print(f"{self.nome} venceu um desafio! Pontos: {self.pontos}")

class JogadorPremium(Jogador):
    def vencer_desafio(self):
        self.pontos += 20  # Bônus: ganha o dobro
        print(f"{self.nome} (Premium) venceu um desafio! Pontos: {self.pontos}")

j1 = Jogador("emisu")
j2 = JogadorPremium("karen")

j1.vencer_desafio() 
j2.vencer_desafio()  


