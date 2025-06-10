class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} diz: Olá, viajante!")

class NPC(Personagem):
    def falar(self):
        print(f"{self.nome} diz: Bem-vindo à nossa vila. Precisa de ajuda?")


p = Personagem("Herói")
npc = NPC("Velho Sábio")

p.falar()    
npc.falar() 
