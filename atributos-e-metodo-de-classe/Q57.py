class Jogador:
    _total_de_jogadores = 0
    def __init__(self, nome, camisa):
        self.nome = nome
        self.camisa = camisa
        Jogador._total_de_jogadores += 1
        print(f"-> Jogador '{self.nome}' foi criado. Total agora: {Jogador._total_de_jogadores}")

    @classmethod
    def exibir_total_jogadores(cls):
        return cls._total_de_jogadores

print(f"Quantidade inicial de jogadores: {Jogador.exibir_total_jogadores()}\n")

print("Criando os primeiros jogadores...")
jogador1 = Jogador("arrascaeta", 10)
jogador2 = Jogador("diego", 10)
print("\n")


total_atual = Jogador.exibir_total_jogadores()
print(f"A quantidade total de jogadores instanciados é: {total_atual}\n")

