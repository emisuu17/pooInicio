class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    
    def atacar(self):
        print(f"Atacando com {self.nome}, causando {self.dano} de dano!")


class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.arma_equipada = None 
    
    def equipar_arma(self, arma):
        self.arma_equipada = arma
        print(f"{self.nome} equipou a arma: {arma.nome}")
    
    def atacar(self):
        if self.arma_equipada:
            self.arma_equipada.atacar()
        else:
            print(f"{self.nome} não tem nenhuma arma equipada!")


espada = Arma("Espada", 25)
arco = Arma("Arco e Flecha", 15)

jogador = Jogador("Arthur")
jogador.atacar()
jogador.equipar_arma(espada) 
jogador.atacar() 
jogador.equipar_arma(arco) 
jogador.atacar()