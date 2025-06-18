# Classe Inimigo
class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        print(f"Inimigo {self.nome} criado!")

    def atacar(self):
        print(f"{self.nome} atacou!")

    def destruir(self):
        print(f"Inimigo {self.nome} destruído!")


class Fase:
    def __init__(self, nome):
        self.nome = nome
        self.inimigos = []  
        print(f"Fase {self.nome} iniciada!")

    def adicionar_inimigo(self, inimigo):
        self.inimigos.append(inimigo)
        print(f"Inimigo {inimigo.nome} adicionado à fase {self.nome}")

    def iniciar(self):
        print(f"Iniciando a fase {self.nome}...")
        for inimigo in self.inimigos:
            inimigo.atacar()

    def finalizar(self):
        print(f"Finalizando a fase {self.nome}...")
        for inimigo in self.inimigos:
            inimigo.destruir()  
        self.inimigos.clear()  


fase1 = Fase("Floresta Sombria")
inimigo1 = Inimigo("Goblin")
inimigo2 = Inimigo("Orc")

fase1.adicionar_inimigo(inimigo1)  
fase1.adicionar_inimigo(inimigo2)
fase1.iniciar()  
fase1.finalizar()  
