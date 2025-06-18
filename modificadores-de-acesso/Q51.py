class Jogador:
    def __init__(self, nome):
        self.nome = nome
        print(f"Jogador {self.nome} criado!")

    def atacar(self):
        print(f"{self.nome} está atacando!")

    def curar(self):
        print(f"{self.nome} está curando!")


class Guilda:
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []  
        print(f"Guilda {self.nome} criada!")

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador.nome} adicionado à guilda {self.nome}.")

    def listar_jogadores(self):
        if self.jogadores:
            print(f"Jogadores da guilda {self.nome}:")
            for jogador in self.jogadores:
                print(f"- {jogador.nome}")
        else:
            print(f"A guilda {self.nome} não tem jogadores.")


jogador1 = Jogador("emisu")
jogador2 = Jogador("karen")
jogador3 = Jogador("caio")

guilda = Guilda("Cavaleiros de Ouro")
guilda.adicionar_jogador(jogador1)  
guilda.adicionar_jogador(jogador2)
guilda.adicionar_jogador(jogador3)

guilda.listar_jogadores() 
