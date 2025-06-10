class Aliado:
    def __init__(self, nome):
        self.nome = nome

    def usar_habilidade(self):
        print(f"{self.nome} usa uma habilidade.")

class Mago(Aliado):
    def usar_habilidade(self):
        print(f"{self.nome} lança uma magia")


class Guerreiro(Aliado):
    def usar_habilidade(self):
        print(f"{self.nome} usa um golpe poderoso com a espada!")

aliado1 = Mago("Schierke")
aliado2 = Guerreiro("Guts")

aliado1.usar_habilidade()   
aliado2.usar_habilidade()  
