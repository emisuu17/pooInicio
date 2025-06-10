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
        print(f"Jogador '{jogador}' conectado.")

    def iniciar(self):
        print(f"Iniciando o jogo multiplayer: {self.nome}")
        if self.jogadores:
            print("Jogadores conectados:")
            for j in self.jogadores:
                print(f"- {j}")
        else:
            print("Nenhum jogador conectado.")

jogo = JogoMultiplayer("Batalha Online")
jogo.adicionar_jogador("Lucas")
jogo.adicionar_jogador("Ana")
jogo.iniciar()
