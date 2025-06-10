class Jogo:
    def __init__(self, nome):
        self.nome = nome

    def iniciar(self):
        print(f"Iniciando o jogo: {self.nome}")

class JogoMultiplayer(Jogo):
    def __init__(self, nome):
        super().__init__(nome)
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"Jogador {jogador} adicionado ao jogo.")

    def listar_jogadores(self):
        print("Jogadores no jogo:")
        for jogador in self.jogadores:
            print(f"- {jogador}")

jogo = JogoMultiplayer("Batalha Online")
jogo.iniciar()

jogo.adicionar_jogador("Alice")
jogo.adicionar_jogador("Bob")

jogo.listar_jogadores()

