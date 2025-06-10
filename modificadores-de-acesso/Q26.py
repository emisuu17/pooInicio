class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def atacar(self):
        print(f"{self.nome} atacou!")

class NPC(Personagem):
    def atacar(self):
        print(f"{self.nome} é um NPC e não pode atacar.")
        
heroi = Personagem("Herói")
npc = NPC("Aldeão")

heroi.atacar()  
npc.atacar()    

