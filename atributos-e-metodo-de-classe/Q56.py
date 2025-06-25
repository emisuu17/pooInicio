class Jogador:
    total_jogadores = 0

    def __init__(self, nome, pontuacao=0):
        self.nome = nome
        self.pontuacao = pontuacao
        Jogador.total_jogadores += 1

    def __str__(self):
        return f"Jogador: {self.nome}, Pontuação: {self.pontuacao}"

# Exemplo de uso:
jogador1 = Jogador("Alice")
jogador2 = Jogador("Bob", 100)
jogador3 = Jogador("Charlie")

print(f"Número total de jogadores criados: {Jogador.total_jogadores}")

print(jogador1)
print(jogador2)
print(jogador3)

jogador4 = Jogador("Emisu", 50)
print(f"Número total de jogadores criados: {Jogador.total_jogadores}")